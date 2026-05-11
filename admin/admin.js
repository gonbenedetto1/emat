// ════════════════════════════════════════════════
// EMAT — Admin Panel
// ════════════════════════════════════════════════

// ── Supabase config ──
const SUPABASE_URL  = 'https://imovmcyiegrgwhxibcjf.supabase.co';
const SUPABASE_ANON = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imltb3ZtY3lpZWdyZ3doeGliY2pmIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzY5MDk1NTYsImV4cCI6MjA5MjQ4NTU1Nn0.Bnr_IF6xOHfRXi0lUmoBDlKBWUaUhaUdeP_BgjZhokY';
const STORAGE_BUCKET = 'emat-public';

const sb = supabase.createClient(SUPABASE_URL, SUPABASE_ANON);

// ── State ──
let currentUser = null;
let currentPost = null;        // post being edited (null = new)
let currentImageFile = null;   // file pending upload

// ── Elements ──
const loginScreen   = document.getElementById('login-screen');
const dashboard     = document.getElementById('dashboard');
const loginForm     = document.getElementById('login-form');
const loginError    = document.getElementById('login-error');
const postModal     = document.getElementById('post-modal');

// ════════════════════════════════════════════════
// AUTH
// ════════════════════════════════════════════════
async function checkSession() {
  const { data: { session } } = await sb.auth.getSession();
  if (session) {
    currentUser = session.user;
    showDashboard();
  } else {
    showLogin();
  }
}

function showLogin() {
  loginScreen.classList.remove('hidden');
  dashboard.classList.add('hidden');
}

function showDashboard() {
  loginScreen.classList.add('hidden');
  dashboard.classList.remove('hidden');
  document.getElementById('user-email').textContent = currentUser.email;
  loadPosts();
  loadSettings();
}

loginForm.addEventListener('submit', async e => {
  e.preventDefault();
  loginError.classList.remove('show');
  const btn = document.getElementById('login-btn');
  btn.disabled = true; btn.textContent = 'Entrando…';

  const { data, error } = await sb.auth.signInWithPassword({
    email: document.getElementById('login-email').value,
    password: document.getElementById('login-password').value
  });

  btn.disabled = false; btn.textContent = 'Entrar';

  if (error) {
    loginError.textContent = 'Email o contraseña incorrectos.';
    loginError.classList.add('show');
    return;
  }
  currentUser = data.user;
  showDashboard();
});

document.getElementById('logout-btn').addEventListener('click', async () => {
  await sb.auth.signOut();
  currentUser = null;
  showLogin();
  loginForm.reset();
});

// ════════════════════════════════════════════════
// TABS
// ════════════════════════════════════════════════
document.querySelectorAll('.tab').forEach(t => {
  t.addEventListener('click', () => {
    document.querySelectorAll('.tab').forEach(x => x.classList.remove('active'));
    document.querySelectorAll('.tab-panel').forEach(x => x.classList.remove('active'));
    t.classList.add('active');
    document.querySelector(`[data-panel="${t.dataset.tab}"]`).classList.add('active');
  });
});

// ════════════════════════════════════════════════
// POSTS — list + CRUD
// ════════════════════════════════════════════════
async function loadPosts() {
  const grid    = document.getElementById('posts-grid');
  const loading = document.getElementById('posts-loading');
  const empty   = document.getElementById('posts-empty');
  loading.classList.remove('hidden');
  grid.innerHTML = '';
  empty.classList.add('hidden');

  const { data, error } = await sb
    .from('emat_posts')
    .select('*')
    .order('publish_date', { ascending: false });

  loading.classList.add('hidden');

  if (error) { toast('Error cargando notas: ' + error.message, true); return; }
  if (!data || !data.length) { empty.classList.remove('hidden'); return; }

  data.forEach(post => grid.appendChild(buildPostCard(post)));
}

function buildPostCard(post) {
  const card = document.createElement('div');
  card.className = 'post-card';
  card.onclick = () => openPostEditor(post);
  const img = post.image_url || '';
  card.innerHTML = `
    <div class="post-card-img" style="background-image:url('${img.replace(/'/g, "\\'")}')">
      <span class="post-card-status ${post.published ? 'published' : 'draft'}">
        ${post.published ? '● Publicada' : '○ Borrador'}
      </span>
    </div>
    <div class="post-card-body">
      <div class="post-card-cat">${post.category}</div>
      <h3>${escapeHtml(post.title)}</h3>
      <div class="post-card-meta">
        <span>${formatDate(post.publish_date)}</span>
        <span>${post.author || ''}</span>
      </div>
    </div>`;
  return card;
}

document.getElementById('new-post-btn').onclick = () => openPostEditor(null);

function openPostEditor(post) {
  currentPost = post;
  currentImageFile = null;
  document.getElementById('post-modal-title').textContent = post ? 'Editar nota' : 'Nueva nota';
  document.getElementById('post-delete-btn').classList.toggle('hidden', !post);

  document.getElementById('p-title').value = post?.title || '';
  document.getElementById('p-slug').value = post?.slug || '';
  document.getElementById('p-category').value = post?.category || 'Novedades';
  document.getElementById('p-date').value = post?.publish_date || new Date().toISOString().slice(0, 10);
  document.getElementById('p-author').value = post?.author || 'Equipo EMAT';
  document.getElementById('p-excerpt').value = post?.excerpt || '';
  document.getElementById('p-body').value = post?.body || '';
  document.getElementById('p-published').checked = post?.published ?? true;

  const prev = document.getElementById('p-image-preview');
  if (post?.image_url) {
    prev.style.backgroundImage = `url('${post.image_url}')`;
    prev.textContent = '';
  } else {
    prev.style.backgroundImage = '';
    prev.textContent = 'Sin imagen';
  }
  document.getElementById('p-image').value = '';

  postModal.classList.remove('hidden');
  updatePreview();
}

function closePostEditor() {
  postModal.classList.add('hidden');
  currentPost = null;
  currentImageFile = null;
}

document.getElementById('post-modal-close').onclick = closePostEditor;
document.getElementById('post-cancel-btn').onclick = closePostEditor;
postModal.onclick = e => { if (e.target === postModal) closePostEditor(); };

// ── Auto-slug from title ──
document.getElementById('p-title').addEventListener('input', e => {
  const slugInput = document.getElementById('p-slug');
  if (!slugInput.dataset.manual) slugInput.value = slugify(e.target.value);
  updatePreview();
});
document.getElementById('p-slug').addEventListener('input', e => {
  e.target.dataset.manual = '1';
  e.target.value = slugify(e.target.value);
});

// ── Image preview ──
document.getElementById('p-image').addEventListener('change', e => {
  const file = e.target.files[0];
  if (!file) return;
  currentImageFile = file;
  const reader = new FileReader();
  reader.onload = ev => {
    const prev = document.getElementById('p-image-preview');
    prev.style.backgroundImage = `url('${ev.target.result}')`;
    prev.textContent = '';
    updatePreview(ev.target.result);
  };
  reader.readAsDataURL(file);
});

// ── Live preview ──
['p-title', 'p-category', 'p-date', 'p-author', 'p-excerpt', 'p-body']
  .forEach(id => document.getElementById(id).addEventListener('input', () => updatePreview()));

function updatePreview(localImg) {
  const img = localImg
    || (document.getElementById('p-image-preview').style.backgroundImage || '').replace(/^url\(['"]?(.*?)['"]?\)$/, '$1')
    || '';
  const html = renderPostPreview({
    title: document.getElementById('p-title').value || '[Sin título]',
    category: document.getElementById('p-category').value,
    date: formatDate(document.getElementById('p-date').value),
    author: document.getElementById('p-author').value,
    body: document.getElementById('p-body').value,
    image: img
  });
  document.getElementById('preview-iframe').srcdoc = html;
}

function renderPostPreview({ title, category, date, author, body, image }) {
  const bodyHtml = marked.parse(body || '');
  const imgBlock = image ? `<img src="${image}" style="width:100%;height:280px;object-fit:cover;border-radius:6px;margin-bottom:24px">` : '';
  return `<!DOCTYPE html><html><head><meta charset="UTF-8">
<style>
  body{font-family:'Montserrat',sans-serif;color:#3a3630;padding:32px;max-width:680px;margin:0 auto;line-height:1.6;font-size:15px}
  .meta{font-size:12px;color:#787068;margin-bottom:6px;letter-spacing:.5px}
  .meta .cat{background:#2a6e37;color:#fff;padding:3px 10px;border-radius:3px;font-weight:700;text-transform:uppercase;font-size:10px;letter-spacing:1px}
  h1{font-size:30px;font-weight:800;color:#18150f;letter-spacing:-.5px;line-height:1.15;margin:8px 0 22px}
  h2{font-size:22px;font-weight:800;color:#18150f;margin:30px 0 12px}
  h3{font-size:17px;font-weight:700;color:#18150f;margin:24px 0 8px}
  p{margin-bottom:14px}
  ul,ol{margin:0 0 16px 20px}
  li{margin-bottom:6px}
  blockquote{border-left:3px solid #2a6e37;padding:10px 16px;background:#f0f8f1;font-style:italic;margin:18px 0;border-radius:0 4px 4px 0}
  a{color:#2a6e37}
  img{max-width:100%;border-radius:6px;margin:18px 0}
</style></head><body>
<div class="meta"><span class="cat">${category}</span> · ${date} · ${author}</div>
<h1>${escapeHtml(title)}</h1>
${imgBlock}
${bodyHtml}
</body></html>`;
}

// ── Save post ──
document.getElementById('post-save-btn').onclick = async () => {
  const btn = document.getElementById('post-save-btn');
  btn.disabled = true; btn.textContent = 'Guardando…';

  try {
    let imageUrl = currentPost?.image_url || null;

    // Upload new image if selected
    if (currentImageFile) {
      const slug = document.getElementById('p-slug').value || `post-${Date.now()}`;
      const ext = currentImageFile.name.split('.').pop().toLowerCase();
      const path = `posts/${slug}-${Date.now()}.${ext}`;
      const { error: upErr } = await sb.storage.from(STORAGE_BUCKET).upload(path, currentImageFile, { upsert: true });
      if (upErr) throw upErr;
      const { data: { publicUrl } } = sb.storage.from(STORAGE_BUCKET).getPublicUrl(path);
      imageUrl = publicUrl;
    }

    const payload = {
      slug: document.getElementById('p-slug').value,
      title: document.getElementById('p-title').value,
      category: document.getElementById('p-category').value,
      excerpt: document.getElementById('p-excerpt').value || null,
      body: document.getElementById('p-body').value,
      author: document.getElementById('p-author').value || 'Equipo EMAT',
      publish_date: document.getElementById('p-date').value,
      published: document.getElementById('p-published').checked,
      image_url: imageUrl
    };

    if (!payload.slug || !payload.title || !payload.body) {
      throw new Error('Faltan campos: título, slug y cuerpo son obligatorios.');
    }

    let result;
    if (currentPost) {
      result = await sb.from('emat_posts').update(payload).eq('id', currentPost.id).select().single();
    } else {
      result = await sb.from('emat_posts').insert(payload).select().single();
    }
    if (result.error) throw result.error;

    toast(currentPost ? 'Nota actualizada ✓' : 'Nota creada ✓');
    closePostEditor();
    loadPosts();
  } catch (err) {
    toast(err.message || 'Error al guardar', true);
  } finally {
    btn.disabled = false; btn.textContent = 'Guardar nota';
  }
};

// ── Delete post ──
document.getElementById('post-delete-btn').onclick = async () => {
  if (!currentPost) return;
  if (!confirm(`¿Eliminar la nota "${currentPost.title}"?\n\nEsta acción no se puede deshacer.`)) return;

  const { error } = await sb.from('emat_posts').delete().eq('id', currentPost.id);
  if (error) { toast(error.message, true); return; }

  toast('Nota eliminada');
  closePostEditor();
  loadPosts();
};

// ════════════════════════════════════════════════
// SETTINGS
// ════════════════════════════════════════════════
const SETTING_LABELS = {
  precio_kg:        { label: 'Precio por kg (ARS)', help: 'Precio del material por kilo. Impacta en el cálculo del cotizador.' },
  whatsapp_number:  { label: 'Número de WhatsApp', help: 'Formato internacional sin + ni espacios. Ej: 5493515555555' },
  contact_email:    { label: 'Email de contacto', help: 'Donde llegan las consultas del formulario.' },
  linkedin_url:     { label: 'Link de LinkedIn', help: 'URL completa al perfil de la empresa.' },
  instagram_url:    { label: 'Link de Instagram', help: 'URL completa al perfil.' }
};

async function loadSettings() {
  const loading = document.getElementById('settings-loading');
  const form    = document.getElementById('settings-form');
  loading.classList.remove('hidden');
  form.classList.add('hidden');
  form.innerHTML = '';

  const { data, error } = await sb.from('emat_settings').select('*').order('key');
  loading.classList.add('hidden');

  if (error) { toast('Error: ' + error.message, true); return; }

  const settings = {};
  data.forEach(row => settings[row.key] = row.value);

  // Render fields based on known keys, plus any extra keys
  const keys = [...new Set([...Object.keys(SETTING_LABELS), ...Object.keys(settings)])];
  keys.forEach(key => {
    const meta = SETTING_LABELS[key] || { label: key, help: '' };
    const div = document.createElement('div');
    div.className = 'field';
    div.innerHTML = `
      <label>${meta.label}</label>
      <input type="text" name="${key}" value="${escapeHtml(settings[key] ?? '')}">
      ${meta.help ? `<div class="help">${meta.help}</div>` : ''}
    `;
    form.appendChild(div);
  });

  const actions = document.createElement('div');
  actions.className = 'actions';
  actions.innerHTML = `<button type="submit" class="btn btn-primary">Guardar configuración</button>`;
  form.appendChild(actions);

  form.classList.remove('hidden');

  form.onsubmit = async e => {
    e.preventDefault();
    const btn = form.querySelector('button[type=submit]');
    btn.disabled = true; btn.textContent = 'Guardando…';

    const updates = [];
    form.querySelectorAll('input[name]').forEach(inp => {
      updates.push({ key: inp.name, value: inp.value });
    });

    const { error } = await sb.from('emat_settings').upsert(updates);

    btn.disabled = false; btn.textContent = 'Guardar configuración';
    if (error) toast(error.message, true);
    else toast('Configuración guardada ✓');
  };
}

// ════════════════════════════════════════════════
// HELPERS
// ════════════════════════════════════════════════
function slugify(s) {
  return (s || '').toLowerCase()
    .normalize('NFD').replace(/[̀-ͯ]/g, '')
    .replace(/[^a-z0-9\s-]/g, '')
    .trim().replace(/\s+/g, '-');
}

function formatDate(iso) {
  if (!iso) return '';
  const m = ['Ene','Feb','Mar','Abr','May','Jun','Jul','Ago','Sep','Oct','Nov','Dic'];
  const [y, mo, d] = iso.split('-');
  return `${parseInt(d)} ${m[parseInt(mo)-1]} ${y}`;
}

function escapeHtml(s) {
  return String(s ?? '').replace(/[&<>"']/g, c =>
    ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c])
  );
}

function toast(msg, isError) {
  const t = document.getElementById('toast');
  t.textContent = msg;
  t.className = 'toast' + (isError ? ' error' : '');
  setTimeout(() => t.classList.add('hidden'), 3500);
}

// ════════════════════════════════════════════════
// INIT
// ════════════════════════════════════════════════
checkSession();
