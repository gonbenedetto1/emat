-- ════════════════════════════════════════════════════════════════════
-- EMAT — Schema para Supabase
-- Correr este SQL una sola vez en Supabase Dashboard → SQL Editor → New Query
-- Prefijo emat_ en todas las tablas porque la base se comparte con otros proyectos.
-- ════════════════════════════════════════════════════════════════════

-- ──────────────────────────────────────────────
-- 1. TABLA: emat_posts (notas del blog)
-- ──────────────────────────────────────────────
create table if not exists emat_posts (
  id           uuid primary key default gen_random_uuid(),
  slug         text unique not null,
  title        text not null,
  category     text not null default 'Novedades',
  excerpt      text,
  body         text not null,                       -- markdown o HTML
  image_url    text,                                -- URL pública (Supabase Storage o externa)
  author       text default 'Equipo EMAT',
  published    boolean not null default true,
  publish_date date default current_date,
  created_at   timestamptz default now(),
  updated_at   timestamptz default now()
);

create index if not exists emat_posts_slug_idx on emat_posts(slug);
create index if not exists emat_posts_pub_date_idx on emat_posts(published, publish_date desc);

-- ──────────────────────────────────────────────
-- 2. TABLA: emat_settings (configuración del sitio)
-- ──────────────────────────────────────────────
create table if not exists emat_settings (
  key        text primary key,
  value      text not null,
  updated_at timestamptz default now()
);

-- Datos iniciales (modificables desde el panel admin)
insert into emat_settings (key, value) values
  ('precio_kg',        '4500'),
  ('whatsapp_number',  '5493515555555'),
  ('contact_email',    'info@emat.com.ar'),
  ('linkedin_url',     'https://www.linkedin.com/company/emat'),
  ('instagram_url',    'https://www.instagram.com/emat.celulosa')
on conflict (key) do nothing;

-- ──────────────────────────────────────────────
-- 3. TRIGGER: actualizar updated_at automáticamente
-- ──────────────────────────────────────────────
create or replace function emat_set_updated_at()
returns trigger as $$
begin
  new.updated_at = now();
  return new;
end;
$$ language plpgsql;

drop trigger if exists emat_posts_updated_at on emat_posts;
create trigger emat_posts_updated_at
  before update on emat_posts
  for each row execute function emat_set_updated_at();

drop trigger if exists emat_settings_updated_at on emat_settings;
create trigger emat_settings_updated_at
  before update on emat_settings
  for each row execute function emat_set_updated_at();

-- ──────────────────────────────────────────────
-- 4. RLS (Row Level Security)
-- ──────────────────────────────────────────────
alter table emat_posts    enable row level security;
alter table emat_settings enable row level security;

-- Lectura pública
drop policy if exists "emat_posts_select_published" on emat_posts;
create policy "emat_posts_select_published" on emat_posts
  for select using (published = true);

drop policy if exists "emat_settings_select_all" on emat_settings;
create policy "emat_settings_select_all" on emat_settings
  for select using (true);

-- Escritura solo para usuarios autenticados
drop policy if exists "emat_posts_authenticated_write" on emat_posts;
create policy "emat_posts_authenticated_write" on emat_posts
  for all using (auth.role() = 'authenticated')
  with check (auth.role() = 'authenticated');

-- Authenticated users también pueden leer drafts (published=false)
drop policy if exists "emat_posts_authenticated_select_all" on emat_posts;
create policy "emat_posts_authenticated_select_all" on emat_posts
  for select using (auth.role() = 'authenticated');

drop policy if exists "emat_settings_authenticated_write" on emat_settings;
create policy "emat_settings_authenticated_write" on emat_settings
  for all using (auth.role() = 'authenticated')
  with check (auth.role() = 'authenticated');

-- ──────────────────────────────────────────────
-- 5. STORAGE BUCKET (imágenes de notas)
-- ──────────────────────────────────────────────
-- Crear el bucket desde la UI: Storage → New bucket → name: "emat-public" → Public
-- Después correr estas policies:

-- Policy de lectura pública
-- (En Supabase Dashboard → Storage → emat-public → Policies → New policy)
-- Or via SQL:

insert into storage.buckets (id, name, public)
values ('emat-public', 'emat-public', true)
on conflict (id) do nothing;

drop policy if exists "emat_storage_public_read" on storage.objects;
create policy "emat_storage_public_read" on storage.objects
  for select using (bucket_id = 'emat-public');

drop policy if exists "emat_storage_authenticated_write" on storage.objects;
create policy "emat_storage_authenticated_write" on storage.objects
  for insert with check (bucket_id = 'emat-public' and auth.role() = 'authenticated');

drop policy if exists "emat_storage_authenticated_update" on storage.objects;
create policy "emat_storage_authenticated_update" on storage.objects
  for update using (bucket_id = 'emat-public' and auth.role() = 'authenticated');

drop policy if exists "emat_storage_authenticated_delete" on storage.objects;
create policy "emat_storage_authenticated_delete" on storage.objects
  for delete using (bucket_id = 'emat-public' and auth.role() = 'authenticated');

-- ──────────────────────────────────────────────
-- 6. SEED: una nota de ejemplo (opcional, podés eliminarla después)
-- ──────────────────────────────────────────────
insert into emat_posts (slug, title, category, excerpt, body, author)
values (
  'bienvenidos-al-blog-emat',
  '¡Bienvenidos al blog de EMAT!',
  'Novedades',
  'Acá vamos a compartir novedades del sector, casos de obra, conocimiento técnico y reflexiones sobre construcción sustentable.',
  '## Qué van a encontrar acá\n\nEn este blog vamos a publicar regularmente:\n\n- **Casos de obra** reales con datos de rendimiento\n- **Notas técnicas** sobre aislación, eficiencia energética y construcción sustentable\n- **Novedades** del sector y nuevos productos\n- **Tutoriales** para arquitectos, constructoras y propietarios\n\n## Suscribite\n\nMuy pronto vamos a tener una newsletter. Mientras tanto, seguinos en redes para no perderte ninguna publicación.',
  'Equipo EMAT'
)
on conflict (slug) do nothing;

-- ════════════════════════════════════════════════════════════════════
-- LISTO. Ahora:
-- 1. Crear usuario admin: Authentication → Users → Add user
-- 2. Volver al admin panel: /admin/index.html
-- ════════════════════════════════════════════════════════════════════
