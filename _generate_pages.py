"""Generador de páginas estáticas para EMAT.
Crea las 6 páginas nuevas reutilizando un template común.
Ejecutar: python3 _generate_pages.py
"""
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ───────────────────────────────────────────────────────────
# TEMPLATE BASE (compartido por todas las páginas)
# ───────────────────────────────────────────────────────────
def render_page(*, title, description, og_title, og_desc, body_class,
                hero_html, content_html, asset_prefix="", page_url=""):
    """asset_prefix = '' para páginas en raíz, '../' para páginas en /blog/"""
    nav_active_class = ""

    return f'''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<meta name="author" content="EMAT">
<meta name="robots" content="index, follow">
<meta name="theme-color" content="#2a6e37">
<link rel="canonical" href="https://emat.com.ar/{page_url}">
<meta property="og:type" content="website">
<meta property="og:title" content="{og_title}">
<meta property="og:description" content="{og_desc}">
<meta property="og:url" content="https://emat.com.ar/{page_url}">
<meta property="og:locale" content="es_AR">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{og_title}">
<meta name="twitter:description" content="{og_desc}">
<link rel="icon" type="image/png" href="{asset_prefix}assets/img/favicon-32.png">
<link rel="apple-touch-icon" href="{asset_prefix}assets/img/favicon-256.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{asset_prefix}assets/styles.css">
</head>
<body>

<!-- ═══ NAV ═══ -->
<nav id="nav">
  <div class="nav-bar">
    <a class="nav-logo" href="{asset_prefix}index.html">
      <img src="{asset_prefix}assets/logo.png" alt="EMAT" />
    </a>
    <div class="nav-links">
      <a href="{asset_prefix}index.html#prods">Producto</a>
      <a href="{asset_prefix}arquitectos.html">Arquitectos</a>
      <a href="{asset_prefix}constructoras.html">Constructoras</a>
      <a href="{asset_prefix}hogar.html">Hogar</a>
      <a href="{asset_prefix}quienes-somos.html">Nosotros</a>
      <a href="{asset_prefix}blog/index.html">Blog</a>
    </div>
    <div class="nav-r">
      <button class="nav-ham" id="hambtn" onclick="toggleNav()" aria-label="Menú">
        <span></span><span></span><span></span>
      </button>
      <a href="{asset_prefix}index.html#presupuesto" class="nav-cta">Cotizar</a>
    </div>
  </div>
</nav>
<div id="nmob">
  <a href="{asset_prefix}index.html#prods" onclick="closeNav()">Producto</a>
  <a href="{asset_prefix}arquitectos.html" onclick="closeNav()">Arquitectos</a>
  <a href="{asset_prefix}constructoras.html" onclick="closeNav()">Constructoras</a>
  <a href="{asset_prefix}hogar.html" onclick="closeNav()">Hogar</a>
  <a href="{asset_prefix}quienes-somos.html" onclick="closeNav()">Nosotros</a>
  <a href="{asset_prefix}blog/index.html" onclick="closeNav()">Blog</a>
  <a href="{asset_prefix}index.html#presupuesto" class="nm-btn" onclick="closeNav()">Cotizar proyecto</a>
</div>

{hero_html}

{content_html}

<!-- ═══ FOOTER ═══ -->
<footer>
  <div class="wrap">
    <div class="ft">
      <div class="fb">
        <a href="{asset_prefix}index.html" class="fb-logo"><img src="{asset_prefix}assets/logo.png" alt="EMAT" /></a>
        <p>Aislación sustentable con celulosa reciclada. Córdoba, Argentina.</p>
        <div class="fb-chips"><div class="fcc">LEED</div><div class="fcc">EDGE</div></div>
        <div class="fb-social">
          <a href="https://www.linkedin.com/company/emat" target="_blank" rel="noopener" aria-label="LinkedIn">
            <svg viewBox="0 0 24 24" fill="currentColor"><path d="M19 0h-14C2.24 0 0 2.24 0 5v14c0 2.76 2.24 5 5 5h14c2.76 0 5-2.24 5-5V5c0-2.76-2.24-5-5-5zM8 19H5V8h3v11zM6.5 6.73c-.97 0-1.75-.79-1.75-1.76s.78-1.76 1.75-1.76 1.75.79 1.75 1.76-.78 1.76-1.75 1.76zM20 19h-3v-5.6c0-3.37-4-3.11-4 0V19h-3V8h3v1.76c1.4-2.59 7-2.78 7 2.48V19z"/></svg>
          </a>
          <a href="https://www.instagram.com/emat.celulosa" target="_blank" rel="noopener" aria-label="Instagram">
            <svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2.16c3.2 0 3.58.01 4.85.07 1.17.05 1.8.25 2.23.41.56.22.96.48 1.38.9.42.42.68.82.9 1.38.16.42.36 1.06.41 2.23.06 1.27.07 1.65.07 4.85s-.01 3.58-.07 4.85c-.05 1.17-.25 1.8-.41 2.23-.22.56-.48.96-.9 1.38-.42.42-.82.68-1.38.9-.42.16-1.06.36-2.23.41-1.27.06-1.65.07-4.85.07s-3.58-.01-4.85-.07c-1.17-.05-1.8-.25-2.23-.41a3.81 3.81 0 01-1.38-.9 3.81 3.81 0 01-.9-1.38c-.16-.42-.36-1.06-.41-2.23-.06-1.27-.07-1.65-.07-4.85s.01-3.58.07-4.85c.05-1.17.25-1.8.41-2.23.22-.56.48-.96.9-1.38.42-.42.82-.68 1.38-.9.42-.16 1.06-.36 2.23-.41 1.27-.06 1.65-.07 4.85-.07M12 0C8.74 0 8.33.01 7.05.07 5.78.13 4.9.33 4.14.63a5.93 5.93 0 00-2.14 1.39A5.93 5.93 0 00.63 4.14C.33 4.9.13 5.78.07 7.05.01 8.33 0 8.74 0 12s.01 3.67.07 4.95c.06 1.27.26 2.15.56 2.91.31.79.73 1.46 1.39 2.14a5.93 5.93 0 002.14 1.39c.76.3 1.64.5 2.91.56C8.33 23.99 8.74 24 12 24s3.67-.01 4.95-.07c1.27-.06 2.15-.26 2.91-.56a5.93 5.93 0 002.14-1.39c.66-.68 1.08-1.35 1.39-2.14.3-.76.5-1.64.56-2.91.06-1.28.07-1.69.07-4.95s-.01-3.67-.07-4.95c-.06-1.27-.26-2.15-.56-2.91a5.93 5.93 0 00-1.39-2.14A5.93 5.93 0 0019.86.63C19.1.33 18.22.13 16.95.07 15.67.01 15.26 0 12 0z"/><path d="M12 5.84a6.16 6.16 0 100 12.32 6.16 6.16 0 000-12.32zM12 16a4 4 0 110-8 4 4 0 010 8z"/><circle cx="18.41" cy="5.59" r="1.44"/></svg>
          </a>
        </div>
      </div>
      <div class="fc"><h4>Soluciones</h4><ul><li><a href="{asset_prefix}arquitectos.html">Arquitectos</a></li><li><a href="{asset_prefix}constructoras.html">Constructoras</a></li><li><a href="{asset_prefix}hogar.html">Hogar</a></li></ul></div>
      <div class="fc"><h4>Producto</h4><ul><li><a href="{asset_prefix}index.html#perf">Beneficios</a></li><li><a href="{asset_prefix}index.html#apps">Aplicaciones</a></li><li><a href="{asset_prefix}index.html#prods">Productos</a></li><li><a href="{asset_prefix}index.html#presupuesto">Cotizador</a></li></ul></div>
      <div class="fc"><h4>Empresa</h4><ul><li><a href="{asset_prefix}quienes-somos.html">Nosotros</a></li><li><a href="{asset_prefix}blog/index.html">Blog</a></li><li><a href="{asset_prefix}index.html#cont">Contacto</a></li></ul></div>
    </div>
    <div class="fb-bot"><span>© 2026 EMAT — Ecoaislante de Celulosa. Córdoba, Argentina.</span><span>Av. La Voz del Interior 4080</span></div>
  </div>
</footer>

<!-- ═══ WHATSAPP FLOAT ═══ -->
<a class="wa-float" id="wa-float-btn" href="https://wa.me/5493515555555?text=Hola%2C%20me%20comunico%20desde%20la%20web%20de%20EMAT." target="_blank" rel="noopener" aria-label="Contactar por WhatsApp">
  <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
    <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51a12.8 12.8 0 0 0-.57-.01c-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 0 1 2.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0 0 12.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 0 0 5.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 0 0-3.48-8.413z"/>
  </svg>
</a>

<script>
// Scroll reveal
const ro=new IntersectionObserver(ents=>{{ents.forEach((e,i)=>{{if(e.isIntersecting){{setTimeout(()=>e.target.classList.add('in'),i*50);ro.unobserve(e.target)}}}})}},{{threshold:.07}});
document.querySelectorAll('.sr').forEach(el=>ro.observe(el));
// Nav
window.addEventListener('scroll',()=>{{document.querySelector('.nav-bar').style.boxShadow=scrollY>50?'0 2px 20px rgba(0,0,0,.55)':'none'}},{{passive:true}});
function toggleNav(){{document.getElementById('nmob').classList.toggle('open')}}
function closeNav(){{document.getElementById('nmob').classList.remove('open')}}
document.addEventListener('click',e=>{{if(!e.target.closest('#nav')&&!e.target.closest('#nmob'))closeNav()}});
</script>
</body>
</html>'''


# ───────────────────────────────────────────────────────────
# CONTENIDO POR PÁGINA
# ───────────────────────────────────────────────────────────

# Hero genérico para subpáginas (más bajo que el del home, sin video)
def page_hero(eyebrow, h1, sub, cta_label="Cotizar proyecto", cta_href="index.html#presupuesto",
              cta2_label=None, cta2_href=None, bg_image=None):
    cta2 = ""
    if cta2_label:
        cta2 = f'<a href="{cta2_href}" class="btn btn-ow">{cta2_label}</a>'
    bg_style = f' style="background-image:linear-gradient(135deg,rgba(8,26,11,.75) 0%,rgba(16,46,22,.6) 50%,rgba(26,72,34,.55) 100%),url(\'{bg_image}\');background-size:cover;background-position:center"' if bg_image else ''
    return f'''<!-- ═══ HERO PÁGINA ═══ -->
<section id="hero" class="page-hero">
  <div class="page-hero-bg"{bg_style}></div>
  <div class="wrap">
    <div class="hero-c sr">
      <div class="hero-eyebrow"><div class="hero-dot"></div>{eyebrow}</div>
      <h1 class="hero-h1 page-hero-h1">{h1}</h1>
      <p class="hero-sub">{sub}</p>
      <div class="hero-ctas">
        <a href="{cta_href}" class="btn btn-p">{cta_label}</a>
        {cta2}
      </div>
    </div>
  </div>
</section>'''


# ──── ARQUITECTOS ────
arquitectos_content = '''
<!-- Por qué incluir EMAT -->
<section id="perf" class="sec">
  <div class="wrap">
    <div class="sec-hdr sr">
      <div><div class="lbl">Para arquitectos</div><h2 class="h2" style="margin-bottom:0">POR QUÉ ESPECIFICAR EMAT EN TU PROYECTO</h2></div>
    </div>
    <div class="feat-row sr">
      <div class="fi">
        <div class="fi-ico"><svg viewBox="0 0 24 24"><path d="M14 14.76V3.5a2.5 2.5 0 00-5 0v11.26a4.5 4.5 0 105 0z"/></svg></div>
        <strong>Performance térmica certificada</strong><span>Valores λ y R verificables, datos para incluir directamente en tu cálculo de transmitancia.</span>
      </div>
      <div class="fi">
        <div class="fi-ico"><svg viewBox="0 0 24 24"><path d="M3 18v-6a9 9 0 0118 0v6"/><path d="M21 19a2 2 0 01-2 2h-1a2 2 0 01-2-2v-3a2 2 0 012-2h3zM3 19a2 2 0 002 2h1a2 2 0 002-2v-3a2 2 0 00-2-2H3z"/></svg></div>
        <strong>Acústica medible</strong><span>Reducción de 45 a 55 dB. Soluciones específicas para muros divisorios y entrepisos.</span>
      </div>
      <div class="fi">
        <div class="fi-ico"><svg viewBox="0 0 24 24"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg></div>
        <strong>Aporta a LEED y EDGE</strong><span>Material reciclado, baja huella de carbono y producción local: suma puntos en certificaciones.</span>
      </div>
      <div class="fi">
        <div class="fi-ico"><svg viewBox="0 0 24 24"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg></div>
        <strong>Compatible con todo</strong><span>Steel frame, wood frame, mampostería tradicional, cubiertas livianas y entrepisos.</span>
      </div>
      <div class="fi">
        <div class="fi-ico"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 015.83 1c0 2-3 3-3 3M12 17h.01"/></svg></div>
        <strong>Asesoramiento técnico</strong><span>Resolvemos detalles constructivos, encuentros y puentes térmicos en tu proyecto.</span>
      </div>
    </div>
  </div>
</section>

<!-- Sistemas constructivos -->
<section id="apps">
  <div class="apps-2">
    <div class="ap ap-l" style="background-image:linear-gradient(135deg,rgba(16,46,22,.78) 0%,rgba(8,26,11,.68) 100%),url('assets/img/obra-04.jpg');background-size:cover;background-position:center">
      <div class="lbl lbl-w sr">Sistemas constructivos</div>
      <h2 class="h2 h2-w sr">COMPATIBLE CON TODOS LOS SISTEMAS</h2>
      <p class="bod bod-w sr" style="margin-bottom:24px">Desde construcciones tradicionales hasta sistemas industrializados. EMAT se adapta a la lógica constructiva de cada proyecto.</p>
      <ul class="ap-ul sr">
        <li><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg>Steel frame y wood frame (proyectado)</li>
        <li><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg>Mampostería tradicional (inyectado en cámara)</li>
        <li><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg>Cubiertas livianas y entrepisos</li>
        <li><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg>SIP, paneles prefabricados y modulares</li>
        <li><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg>Construcción mixta y sistemas híbridos</li>
      </ul>
    </div>
    <div class="ap ap-r" style="background-image:linear-gradient(135deg,rgba(28,82,40,.78) 0%,rgba(16,46,22,.68) 100%),url('assets/img/obra-08.jpg');background-size:cover;background-position:center">
      <div class="lbl lbl-w sr">Certificaciones</div>
      <h2 class="h2 h2-w sr">SUMA PUNTOS EN LEED Y EDGE</h2>
      <p class="bod bod-w sr" style="margin-bottom:24px">Producción con más del 80% de insumos reciclados, baja energía incorporada y origen local. Aporta directamente a múltiples créditos de certificaciones de construcción sustentable.</p>
      <ul class="ap-ul sr">
        <li><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg>Materials &amp; Resources (LEED MR)</li>
        <li><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg>Energy &amp; Atmosphere (LEED EA)</li>
        <li><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg>Indoor Environmental Quality (LEED EQ)</li>
        <li><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg>EDGE — Energía y Materiales</li>
        <li><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg>Aporta a huella de carbono reducida</li>
      </ul>
    </div>
  </div>
</section>


<!-- Documentación técnica -->
<section class="sec" style="background:var(--n1)">
  <div class="wrap">
    <div class="sec-hdr sr">
      <div><div class="lbl">Documentación</div><h2 class="h2" style="margin-bottom:0">TODO LO QUE NECESITÁS PARA TU PLIEGO</h2></div>
    </div>
    <div class="bs-g sr">
      <div class="bs-c">
        <div class="bs-ico"><svg viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"/><polyline points="14 2 14 8 20 8"/></svg></div>
        <div><h3>Fichas técnicas</h3><p>Hojas de datos con valores de conductividad, densidad, comportamiento al fuego, absorción acústica y más. Listas para anexar al pliego.</p></div>
      </div>
      <div class="bs-c">
        <div class="bs-ico"><svg viewBox="0 0 24 24"><path d="M9 11l3 3L22 4"/><path d="M21 12v7a2 2 0 01-2 2H5a2 2 0 01-2-2V5a2 2 0 012-2h11"/></svg></div>
        <div><h3>Ensayos y certificaciones</h3><p>Resultados de ensayos térmicos, acústicos e ignífugos realizados según normas IRAM e ISO. Documentación oficial disponible.</p></div>
      </div>
      <div class="bs-c">
        <div class="bs-ico"><svg viewBox="0 0 24 24"><path d="M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438 3.42 3.42 0 00-.806 1.946 3.42 3.42 0 01-3.138 3.138 3.42 3.42 0 00-1.946.806 3.42 3.42 0 01-4.438 0 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-3.138-3.138 3.42 3.42 0 00-.806-1.946 3.42 3.42 0 010-4.438 3.42 3.42 0 00.806-1.946 3.42 3.42 0 013.138-3.138z"/></svg></div>
        <div><h3>Manual de instalación</h3><p>Detalles constructivos, encuentros típicos, espesores recomendados según zona climática y tabla de rendimientos por aplicación.</p></div>
      </div>
      <div class="bs-c">
        <div class="bs-ico"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg></div>
        <div><h3>Asesoramiento personalizado</h3><p>Te acompañamos desde el anteproyecto hasta la ejecución. Resolvemos detalles, calculamos rendimientos y validamos especificaciones.</p></div>
      </div>
    </div>
    <div style="text-align:center;margin-top:40px" class="sr">
      <a href="index.html#cont" class="btn btn-p">Solicitar documentación técnica</a>
    </div>
  </div>
</section>

<!-- CTA -->
<section id="ctaf" style="background-image:linear-gradient(135deg,rgba(26,82,40,.92) 0%,rgba(8,26,11,.88) 100%),url(\'assets/img/obra-04.jpg\');background-size:cover;background-position:center;background-color:var(--g4)">
  <div class="wrap" style="text-align:center">
    <h2 class="h2 h2-w sr" style="margin-bottom:18px">¿Estás especificando un proyecto?</h2>
    <p class="bod bod-w sr" style="margin-bottom:32px;max-width:640px;margin-left:auto;margin-right:auto">Contactanos para resolver detalles técnicos, recibir documentación o coordinar una visita a obra.</p>
    <div class="hero-ctas sr" style="justify-content:center">
      <a href="index.html#cont" class="btn btn-w">Contactar al equipo técnico</a>
      <a href="index.html#presupuesto" class="btn btn-ow">Cotizar proyecto</a>
    </div>
  </div>
</section>
'''

# ──── CONSTRUCTORAS ────
constructoras_content = '''
<!-- Beneficios para tu obra -->
<section id="perf" class="sec">
  <div class="wrap">
    <div class="sec-hdr sr">
      <div><div class="lbl">Para constructoras</div><h2 class="h2" style="margin-bottom:0">PRODUCTIVIDAD Y RENDIMIENTO EN OBRA</h2></div>
    </div>
    <div class="feat-row sr">
      <div class="fi">
        <div class="fi-ico"><svg viewBox="0 0 24 24"><path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/></svg></div>
        <strong>Aplicación rápida</strong><span>Cubrí grandes superficies en menos tiempo que con materiales tradicionales en placa o panel.</span>
      </div>
      <div class="fi">
        <div class="fi-ico"><svg viewBox="0 0 24 24"><line x1="12" y1="1" x2="12" y2="23"/><path d="M17 5H9.5a3.5 3.5 0 000 7h5a3.5 3.5 0 010 7H6"/></svg></div>
        <strong>Mejor rendimiento por m²</strong><span>Optimización de costos por cobertura efectiva: menos desperdicio, sin recortes ni juntas.</span>
      </div>
      <div class="fi">
        <div class="fi-ico"><svg viewBox="0 0 24 24"><path d="M21 16V8a2 2 0 00-1-1.73l-7-4a2 2 0 00-2 0l-7 4A2 2 0 003 8v8a2 2 0 001 1.73l7 4a2 2 0 002 0l7-4A2 2 0 0021 16z"/></svg></div>
        <strong>Modalidad a granel</strong><span>Compra por volumen para constructoras con instalación propia. Logística directa desde Córdoba.</span>
      </div>
      <div class="fi">
        <div class="fi-ico"><svg viewBox="0 0 24 24"><path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 00-3-3.87M16 3.13a4 4 0 010 7.75"/></svg></div>
        <strong>Capacitación a instaladores</strong><span>Formación técnica para tu equipo. Aplicación correcta = mejor performance + cero retrabajos.</span>
      </div>
      <div class="fi">
        <div class="fi-ico"><svg viewBox="0 0 24 24"><path d="M3 6l2-2h14l2 2M3 6l9 7 9-7M3 6v12a2 2 0 002 2h14a2 2 0 002-2V6"/></svg></div>
        <strong>Logística confiable</strong><span>Entregas programadas. Stock disponible en planta para abastecer obras grandes sin demoras.</span>
      </div>
    </div>
  </div>
</section>

<!-- Modalidades -->
<section class="sec" style="background:var(--n1)">
  <div class="wrap">
    <div class="sec-hdr sr">
      <div><div class="lbl">Modalidades</div><h2 class="h2" style="margin-bottom:0">CÓMO TRABAJAMOS CON CONSTRUCTORAS</h2></div>
    </div>
    <div class="prods-3 sr">
      <div class="pc">
        <div class="pc-img pi-g" style="background-image:url('assets/img/granel.jpg')"><div class="pc-tag">Volumen</div></div>
        <div class="pc-body"><h3>A granel</h3><span class="pc-sub">Para instalación propia</span><p>Compra por volumen con asesoramiento técnico inicial. Ideal para constructoras con equipo propio capacitado o instaladores subcontratados.</p><a href="index.html#cont" class="pc-lnk">Cotizar por volumen <svg viewBox="0 0 24 24"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg></a></div>
      </div>
      <div class="pc">
        <div class="pc-img pi-dg" style="background-image:url('assets/img/llaveenman.jpg')"><div class="pc-tag">Servicio</div></div>
        <div class="pc-body"><h3>Aplicación llave en mano</h3><span class="pc-sub">Nuestro equipo en tu obra</span><p>Coordinamos la aplicación con nuestro equipo certificado. Cumplimos plazos, te liberamos esa tarea y garantizamos el rendimiento.</p><a href="index.html#cont" class="pc-lnk">Coordinar visita <svg viewBox="0 0 24 24"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg></a></div>
      </div>
      <div class="pc">
        <div class="pc-img pi-dk" style="background-image:url('assets/img/capacitacion.jpg')"><div class="pc-tag">Formación</div></div>
        <div class="pc-body"><h3>Capacitación técnica</h3><span class="pc-sub">Para tu equipo de obra</span><p>Programa de capacitación a instaladores: técnica, espesores, encuentros, controles de calidad. Certificamos la formación.</p><a href="index.html#cont" class="pc-lnk">Solicitar capacitación <svg viewBox="0 0 24 24"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg></a></div>
      </div>
    </div>
  </div>
</section>

<!-- CTA -->
<section id="ctaf" style="background-image:linear-gradient(135deg,rgba(26,82,40,.92) 0%,rgba(8,26,11,.88) 100%),url(\'assets/img/obra-09.jpg\');background-size:cover;background-position:center;background-color:var(--g4)">
  <div class="wrap" style="text-align:center">
    <h2 class="h2 h2-w sr" style="margin-bottom:18px">Sumá EMAT a tu próxima obra</h2>
    <p class="bod bod-w sr" style="margin-bottom:32px;max-width:640px;margin-left:auto;margin-right:auto">Cotizaciones por volumen, condiciones para constructoras y soporte técnico de principio a fin.</p>
    <div class="hero-ctas sr" style="justify-content:center">
      <a href="index.html#cont" class="btn btn-w">Hablar con ventas</a>
      <a href="index.html#presupuesto" class="btn btn-ow">Cotizar proyecto</a>
    </div>
  </div>
</section>
'''

# ──── HOGAR ────
hogar_content = '''
<!-- Por qué aislar tu casa -->
<section id="perf" class="sec">
  <div class="wrap">
    <div class="sec-hdr sr">
      <div><div class="lbl">Para tu hogar</div><h2 class="h2" style="margin-bottom:0">POR QUÉ AISLAR TU CASA CON CELULOSA</h2></div>
    </div>
    <div class="feat-row sr">
      <div class="fi">
        <div class="fi-ico"><svg viewBox="0 0 24 24"><path d="M14 14.76V3.5a2.5 2.5 0 00-5 0v11.26a4.5 4.5 0 105 0z"/></svg></div>
        <strong>Más confort, todo el año</strong><span>Tu casa se mantiene fresca en verano y cálida en invierno, sin cambios bruscos de temperatura.</span>
      </div>
      <div class="fi">
        <div class="fi-ico"><svg viewBox="0 0 24 24"><line x1="12" y1="1" x2="12" y2="23"/><path d="M17 5H9.5a3.5 3.5 0 000 7h5a3.5 3.5 0 010 7H6"/></svg></div>
        <strong>Ahorro real en gas y luz</strong><span>Hasta 40% menos de consumo en calefacción y refrigeración. La inversión se recupera en pocos años.</span>
      </div>
      <div class="fi">
        <div class="fi-ico"><svg viewBox="0 0 24 24"><path d="M3 18v-6a9 9 0 0118 0v6"/><path d="M21 19a2 2 0 01-2 2h-1a2 2 0 01-2-2v-3a2 2 0 012-2h3zM3 19a2 2 0 002 2h1a2 2 0 002-2v-3a2 2 0 00-2-2H3z"/></svg></div>
        <strong>Menos ruido, más descanso</strong><span>Reduce entre 45 y 55 dB el sonido exterior. Ideal si vivís cerca de avenidas o zonas ruidosas.</span>
      </div>
      <div class="fi">
        <div class="fi-ico"><svg viewBox="0 0 24 24"><path d="M20.84 4.61a5.5 5.5 0 00-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 00-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 000-7.78z"/></svg></div>
        <strong>Mejor para tu salud</strong><span>Previene humedad y moho, mejora la calidad del aire interior y reduce alergias respiratorias.</span>
      </div>
      <div class="fi">
        <div class="fi-ico"><svg viewBox="0 0 24 24"><path d="M3 9l9-7 9 7v11a2 2 0 01-2 2H5a2 2 0 01-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg></div>
        <strong>Sumás valor a tu propiedad</strong><span>Una casa eficiente vale más en el mercado. Invertir en aislación es invertir en tu patrimonio.</span>
      </div>
    </div>
  </div>
</section>

<!-- Cómo se aplica -->
<section class="sec" style="background:var(--n1)">
  <div class="wrap">
    <div class="bs-head sr">
      <div class="lbl">Cómo funciona</div>
      <h2 class="h2">SE APLICA SIN ROMPER NADA</h2>
      <p>Si tu casa ya está construida, podemos aislarla por inyección: hacemos perforaciones mínimas en muros y techos, soplamos celulosa en las cavidades existentes y dejamos todo cerrado. Sin escombros, sin obra grande.</p>
    </div>
    <div class="bs-g sr">
      <div class="bs-c">
        <div class="bs-ico"><svg viewBox="0 0 24 24"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg></div>
        <div><h3>1. Diagnóstico inicial</h3><p>Visitamos tu casa, evaluamos qué tipo de muros y techos tenés, y te explicamos qué solución aplica en cada caso.</p></div>
      </div>
      <div class="bs-c">
        <div class="bs-ico"><svg viewBox="0 0 24 24"><line x1="12" y1="1" x2="12" y2="23"/><path d="M17 5H9.5a3.5 3.5 0 000 7h5a3.5 3.5 0 010 7H6"/></svg></div>
        <div><h3>2. Cotización transparente</h3><p>Recibís un presupuesto claro por superficie y por sector (muros, techos, entrepisos). Sin sorpresas.</p></div>
      </div>
      <div class="bs-c">
        <div class="bs-ico"><svg viewBox="0 0 24 24"><path d="M3 9l9-7 9 7v11a2 2 0 01-2 2H5a2 2 0 01-2-2z"/></svg></div>
        <div><h3>3. Aplicación rápida</h3><p>En pocos días dejamos tu casa aislada. Trabajamos con cuidado, dejamos limpio y sin polvo al terminar.</p></div>
      </div>
      <div class="bs-c">
        <div class="bs-ico"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg></div>
        <div><h3>4. Resultado inmediato</h3><p>Desde el primer día notás la diferencia: menos cambios de temperatura, menos ruido y menos consumo en tus boletas.</p></div>
      </div>
    </div>
  </div>
</section>

<!-- Productos relevantes -->
<section id="prods" class="sec">
  <div class="wrap">
    <div class="sec-hdr sr">
      <div><div class="lbl">Soluciones</div><h2 class="h2" style="margin-bottom:0">QUÉ SOLUCIÓN ES PARA TU CASA</h2></div>
    </div>
    <div class="prods-3 sr">
      <div class="pc">
        <div class="pc-img pi-g" style="background-image:url('assets/img/inyectada.jpg')"><div class="pc-tag">Casa existente</div></div>
        <div class="pc-body"><h3>Soplado</h3><span class="pc-sub">Aislás tu casa sin romper paredes</span><p>Si tu casa ya está construida, esta es la solución. Hacemos perforaciones mínimas, soplamos la celulosa adentro y queda invisible.</p><a href="index.html#presupuesto" class="pc-lnk">Cotizar para mi casa <svg viewBox="0 0 24 24"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg></a></div>
      </div>
      <div class="pc">
        <div class="pc-img pi-dg" style="background-image:url('assets/img/proyectada.jpg')"><div class="pc-tag">Construcción nueva</div></div>
        <div class="pc-body"><h3>Proyectado</h3><span class="pc-sub">Para casas en construcción</span><p>Si estás construyendo o ampliando, lo aplicamos durante la obra. Cobertura total, sin puentes térmicos.</p><a href="index.html#presupuesto" class="pc-lnk">Cotizar para obra nueva <svg viewBox="0 0 24 24"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg></a></div>
      </div>
      <div class="pc">
        <div class="pc-img pi-dk" style="background-image:url('assets/img/asesoramiento.jpg')"></div>
        <div class="pc-body"><h3>Asesoramiento</h3><span class="pc-sub">No estás seguro qué necesitás</span><p>Te visitamos sin cargo, evaluamos tu caso y te recomendamos la mejor solución según el tipo de construcción y tu presupuesto.</p><a href="index.html#cont" class="pc-lnk">Pedir visita <svg viewBox="0 0 24 24"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg></a></div>
      </div>
    </div>
  </div>
</section>

<!-- CTA -->
<section id="ctaf" style="background-image:linear-gradient(135deg,rgba(26,82,40,.92) 0%,rgba(8,26,11,.88) 100%),url(\'assets/img/obra-14.jpg\');background-size:cover;background-position:center;background-color:var(--g4)">
  <div class="wrap" style="text-align:center">
    <h2 class="h2 h2-w sr" style="margin-bottom:18px">Tu casa puede ser más confortable</h2>
    <p class="bod bod-w sr" style="margin-bottom:32px;max-width:640px;margin-left:auto;margin-right:auto">Recibí una cotización personalizada. Sin compromiso, sin obras grandes, con resultados desde el primer día.</p>
    <div class="hero-ctas sr" style="justify-content:center">
      <a href="index.html#presupuesto" class="btn btn-w">Cotizar para mi casa</a>
      <a href="index.html#cont" class="btn btn-ow">Pedir asesoramiento</a>
    </div>
  </div>
</section>
'''

# ──── QUIENES SOMOS (placeholder) ────
quienes_content = '''
<!-- Sección 1: Experiencia corporativa -->
<section class="sec" id="historia">
  <div class="wrap">
    <div class="perf-2">
      <div class="sr">
        <div class="lbl">Nuestra historia</div>
        <h2 class="h2">EXPERIENCIA CORPORATIVA<br>APLICADA A UNA<br>CONSTRUCCIÓN MÁS HUMANA</h2>
      </div>
      <div class="sr">
        <p class="bod" style="margin-bottom:18px">EMAT nació de una búsqueda compartida por sus fundadores: <strong>transformar la manera en que construimos y habitamos</strong>.</p>
        <p class="bod">Tras décadas liderando proyectos en grandes corporaciones de la industria y el desarrollo, decidimos volcar toda esa trayectoria en un proyecto con propósito real. Así nació EMAT, una empresa con base en Córdoba dedicada a la aislación térmica y acústica de alta performance.</p>
      </div>
    </div>
  </div>
</section>

<!-- Sección 2: Por qué celulosa proyectada -->
<section class="sec" style="background:var(--n1)">
  <div class="wrap">
    <div class="bs-head sr">
      <div class="lbl">Por qué celulosa</div>
      <h2 class="h2">¿POR QUÉ ELEGIMOS<br>LA CELULOSA PROYECTADA?</h2>
      <p>Nuestra convicción es clara: la construcción debe evolucionar. No se trata solo de construir más, sino de <strong>construir mejor</strong>. Los espacios que habitamos impactan directamente en nuestra salud y en el medio ambiente.</p>
      <p style="margin-top:14px">Como especialistas en celulosa reciclada, desarrollamos soluciones que permiten:</p>
    </div>
    <div class="bs-g sr">
      <div class="bs-c">
        <div class="bs-ico"><svg viewBox="0 0 24 24"><path d="M14 14.76V3.5a2.5 2.5 0 00-5 0v11.26a4.5 4.5 0 105 0z"/></svg></div>
        <div><h3>Eficiencia energética</h3><p>Reducción drástica del consumo de climatización en cada proyecto.</p></div>
      </div>
      <div class="bs-c">
        <div class="bs-ico"><svg viewBox="0 0 24 24"><path d="M3 18v-6a9 9 0 0118 0v6"/><path d="M21 19a2 2 0 01-2 2h-1a2 2 0 01-2-2v-3a2 2 0 012-2h3zM3 19a2 2 0 002 2h1a2 2 0 002-2v-3a2 2 0 00-2-2H3z"/></svg></div>
        <div><h3>Confort térmico y acústico</h3><p>Silencio y temperatura estable todo el año, en cualquier estación.</p></div>
      </div>
      <div class="bs-c">
        <div class="bs-ico"><svg viewBox="0 0 24 24"><path d="M21 12a9 9 0 11-6.219-8.56"/><polyline points="23 4 12 15 9 12"/></svg></div>
        <div><h3>Economía circular</h3><p>Transformamos papel reciclado en un material de construcción premium.</p></div>
      </div>
      <div class="bs-c">
        <div class="bs-ico"><svg viewBox="0 0 24 24"><path d="M3 9l9-7 9 7v11a2 2 0 01-2 2H5a2 2 0 01-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg></div>
        <div><h3>Sustentabilidad</h3><p>Reducción real de la huella de carbono en cada obra que intervenimos.</p></div>
      </div>
    </div>
  </div>
</section>

<!-- Sección 3: Aliado estratégico -->
<section class="sec" id="aliado">
  <div class="wrap">
    <div class="perf-2">
      <div class="sr">
        <div class="lbl">Nuestro rol</div>
        <h2 class="h2">TU ALIADO<br>ESTRATÉGICO<br>EN OBRA</h2>
      </div>
      <div class="sr">
        <p class="bod" style="margin-bottom:18px">En EMAT no solo fabricamos y proveemos el producto. Nuestro valor diferencial es el <strong>asesoramiento técnico integral</strong>.</p>
        <p class="bod">Trabajamos codo a codo con arquitectos, constructoras y desarrolladores, integrando la aislación desde la etapa de proyecto para garantizar resultados óptimos. Nos mueve la visión de crear espacios más eficientes, saludables y preparados para el futuro.</p>
      </div>
    </div>
  </div>

  <!-- Equipo: directores -->
  <div class="wrap">
    <div class="team-grid sr">
      <div class="team-c">
        <div class="team-photo"><img src="assets/img/andres.jpg" alt="Cr. Andrés Brandan" style="object-position: center 12%" /></div>
        <strong>Cr. Andrés Brandan</strong>
        <span>Director Comercial</span>
      </div>
      <div class="team-c">
        <div class="team-photo"><img src="assets/img/pablo.jpg" alt="Ing. Pablo Raimondo" style="object-position: center 12%" /></div>
        <strong>Ing. Pablo Raimondo</strong>
        <span>Director de Producción</span>
      </div>
      <div class="team-c">
        <div class="team-photo"><img src="assets/img/tristan.jpg" alt="Ing. Tristán Ríos Carranza" /></div>
        <strong>Ing. Tristán Ríos Carranza</strong>
        <span>Director Comercial</span>
      </div>
      <div class="team-c">
        <div class="team-photo"><img src="assets/img/esteban.jpg" alt="Ing. Esteban Nieto" /></div>
        <strong>Ing. Esteban Nieto</strong>
        <span>Director Administrativo y Financiero</span>
      </div>
    </div>
  </div>

  <!-- Imagen nosotros al final de la sección -->
  <div class="nosotros-img sr">
    <img src="assets/img/nosotros.jpg" alt="Equipo EMAT" />
  </div>

  <!-- Cierre -->
  <div class="wrap">
    <div class="qs-cierre sr">
      <p>EMAT no busca solamente aislar estructuras;<br><strong>buscamos impulsar una nueva forma de vivir.</strong></p>
    </div>
  </div>
</section>

<!-- CTA -->
<section id="ctaf" style="background-image:linear-gradient(135deg,rgba(26,82,40,.92) 0%,rgba(8,26,11,.88) 100%),url(\'assets/img/obra-10.jpg\');background-size:cover;background-position:center;background-color:var(--g4)">
  <div class="wrap" style="text-align:center">
    <h2 class="h2 h2-w sr" style="margin-bottom:18px">Construyamos juntos</h2>
    <p class="bod bod-w sr" style="margin-bottom:32px;max-width:640px;margin-left:auto;margin-right:auto">Si te interesa lo que hacemos, escribinos. Estamos siempre abiertos a nuevas obras, alianzas y conversaciones.</p>
    <div class="hero-ctas sr" style="justify-content:center">
      <a href="index.html#cont" class="btn btn-w">Contactanos</a>
      <a href="blog/index.html" class="btn btn-ow">Leer el blog</a>
    </div>
  </div>
</section>
'''

# ──── BLOG ────
def blog_post_card(slug, category, title, excerpt, date, image="../assets/img/obra-01.jpg"):
    return f'''<a href="{slug}.html" class="bp-card sr">
        <div class="bp-img" style="background-image:url('{image}')"></div>
        <div class="bp-body">
          <div class="bp-meta"><span class="bp-cat">{category}</span><span class="bp-date">{date}</span></div>
          <h3>{title}</h3>
          <p>{excerpt}</p>
          <span class="pc-lnk">Leer nota <svg viewBox="0 0 24 24"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg></span>
        </div>
      </a>'''

blog_index_content = f'''
<style>
.bp-grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:28px;margin-bottom:48px}}
.bp-card{{display:flex;flex-direction:column;background:var(--n0);border:1px solid var(--n2);border-radius:8px;overflow:hidden;text-decoration:none;color:inherit;transition:all var(--ease)}}
.bp-card:hover{{border-color:var(--g2);box-shadow:0 8px 28px rgba(26,82,40,.08);transform:translateY(-3px)}}
.bp-img{{height:200px;background-size:cover;background-position:center;background-color:var(--g5);position:relative}}
.bp-img::after{{content:'';position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,0) 50%,rgba(0,0,0,.25));pointer-events:none}}
.bp-body{{padding:24px;flex:1;display:flex;flex-direction:column}}
.bp-meta{{display:flex;justify-content:space-between;align-items:center;margin-bottom:12px}}
.bp-cat{{background:var(--g0);color:var(--g3);font-size:11px;font-weight:700;letter-spacing:1.2px;text-transform:uppercase;padding:4px 10px;border-radius:3px}}
.bp-date{{font-size:12px;color:var(--n4)}}
.bp-card h3{{font-size:17px;font-weight:800;color:var(--n5);margin-bottom:10px;line-height:1.3}}
.bp-card p{{font-size:14px;color:var(--n4);line-height:1.6;flex:1;margin-bottom:14px}}
.bp-filters{{display:flex;justify-content:center;gap:10px;flex-wrap:wrap;margin-bottom:40px}}
.bp-filt{{background:var(--n0);border:1px solid var(--n2);color:var(--n5);font-size:13px;font-weight:600;padding:8px 18px;border-radius:20px;cursor:pointer;transition:all var(--ease)}}
.bp-filt:hover,.bp-filt.active{{background:var(--g3);color:var(--n0);border-color:var(--g3)}}
@media(max-width:960px){{.bp-grid{{grid-template-columns:repeat(2,1fr)}}}}
@media(max-width:600px){{.bp-grid{{grid-template-columns:1fr}}}}
</style>

<section class="sec">
  <div class="wrap">
    <div class="bp-filters sr">
      <button class="bp-filt active">Todos</button>
      <button class="bp-filt">Sustentabilidad</button>
      <button class="bp-filt">Construcción</button>
      <button class="bp-filt">Casos</button>
      <button class="bp-filt">Novedades</button>
    </div>
    <div class="bp-grid">
      {blog_post_card("post-ejemplo", "Sustentabilidad", "Por qué la celulosa reciclada es el futuro de la aislación", "Una mirada profunda a cómo el papel reciclado se convierte en uno de los aislantes más eficientes del mercado, con menor huella de carbono que cualquier alternativa convencional.", "29 Abr 2026", "../assets/img/obra-01.jpg")}
      {blog_post_card("post-ejemplo", "Construcción", "Steel frame y aislación: cómo lograr el máximo rendimiento", "Detalles constructivos, espesores recomendados y errores comunes al aislar viviendas en sistema steel frame. Una guía técnica práctica.", "22 Abr 2026", "../assets/img/obra-04.jpg")}
      {blog_post_card("post-ejemplo", "Casos", "Caso de obra: vivienda eficiente en las sierras de Córdoba", "Cómo una casa de 180 m² logró reducir un 45% el consumo de calefacción combinando diseño bioclimático con aislación de celulosa.", "15 Abr 2026", "../assets/img/obra-08.jpg")}
      {blog_post_card("post-ejemplo", "Novedades", "EMAT certifica nuevos ensayos térmicos según norma IRAM", "Acabamos de obtener nuevos ensayos que validan el rendimiento de nuestros productos. Te contamos qué significan y cómo usarlos en tu pliego.", "08 Abr 2026", "../assets/img/obra-06.jpg")}
      {blog_post_card("post-ejemplo", "Sustentabilidad", "Economía circular en la construcción: del papel al aislante", "El recorrido completo del material: desde que entra a planta como papel descartado hasta que sale como solución de alta performance.", "01 Abr 2026", "../assets/img/obra-13.jpg")}
      {blog_post_card("post-ejemplo", "Construcción", "Aislación acústica: cómo elegir el material correcto", "No todos los aislantes funcionan igual contra el ruido. Comparamos celulosa proyectada con alternativas tradicionales en distintos escenarios.", "25 Mar 2026", "../assets/img/obra-11.jpg")}
    </div>
    <p class="bod sr" style="text-align:center;margin-top:24px;color:var(--n4);font-style:italic">Las notas mostradas son ejemplos. Reemplazá el contenido por las notas reales cargando archivos HTML en la carpeta /blog/.</p>
  </div>
</section>

'''

# ──── BLOG POST EJEMPLO ────
blog_post_content = '''
<style>
.post-meta{display:flex;gap:14px;align-items:center;margin-bottom:18px;font-size:13px;color:rgba(255,255,255,.7)}
.post-meta .bp-cat{background:rgba(255,255,255,.15);color:var(--n0)}
.post-body{max-width:780px;margin:0 auto;padding:64px 24px}
.post-body p{font-size:17px;line-height:1.8;color:var(--n5);margin-bottom:22px}
.post-body h2{font-size:28px;font-weight:800;color:var(--n6);margin:48px 0 18px;letter-spacing:-.4px}
.post-body h3{font-size:22px;font-weight:700;color:var(--n6);margin:36px 0 14px}
.post-body ul{margin:0 0 22px 22px}
.post-body li{font-size:17px;line-height:1.8;color:var(--n5);margin-bottom:8px}
.post-body blockquote{border-left:4px solid var(--g3);padding:18px 24px;background:var(--g0);font-size:18px;font-style:italic;color:var(--n5);margin:32px 0;border-radius:0 6px 6px 0}
.post-body .img-placeholder{background:var(--n2);height:380px;display:flex;align-items:center;justify-content:center;color:var(--n4);font-style:italic;margin:32px 0;border-radius:6px}
.post-author{display:flex;align-items:center;gap:14px;padding:24px;border:1px solid var(--n2);border-radius:8px;margin:48px 0 24px}
.post-author-img{width:56px;height:56px;border-radius:50%;background:var(--g3);color:var(--n0);display:flex;align-items:center;justify-content:center;font-weight:800;font-size:18px;flex-shrink:0}
.post-author-name{font-weight:700;color:var(--n5);margin-bottom:4px}
.post-author-bio{font-size:13px;color:var(--n4)}
.post-back{display:inline-flex;align-items:center;gap:6px;color:var(--g3);text-decoration:none;font-weight:600;font-size:14px;margin-bottom:24px}
.post-back svg{width:14px;height:14px;stroke:currentColor;fill:none;stroke-width:2.5}
</style>

<article class="post-body">
  <a href="index.html" class="post-back"><svg viewBox="0 0 24 24"><line x1="19" y1="12" x2="5" y2="12"/><polyline points="12 19 5 12 12 5"/></svg>Volver al blog</a>

  <p><em>Esta nota es un template de ejemplo. Reemplazá el contenido y duplicá este archivo (con un slug nuevo) cada vez que cargues una nota.</em></p>

  <p>La aislación con celulosa reciclada está cambiando la forma en que pensamos los materiales en construcción. No es una tendencia: es una respuesta concreta a tres desafíos que hoy enfrenta cualquier obra: <strong>eficiencia energética, costos operativos y huella ambiental</strong>.</p>

  <img src="../assets/img/obra-01.jpg" alt="Aplicación de celulosa proyectada" style="width:100%;height:auto;border-radius:6px;margin:32px 0">

  <h2>Qué es la celulosa proyectada</h2>
  <p>La celulosa proyectada es un material aislante fabricado a partir de papel reciclado, tratado con sales de bórax para resistir el fuego, los hongos y los insectos. Se aplica directamente sobre la estructura mediante equipos especializados, formando una capa continua que rellena cada espacio sin dejar puentes térmicos.</p>

  <p>A diferencia de los paneles o las placas, no genera juntas ni recortes, y se adapta a geometrías complejas. Esto la hace especialmente eficiente en entrepisos, cubiertas inclinadas y muros con instalaciones internas.</p>

  <h2>Por qué importa hoy</h2>

  <h3>1. Eficiencia energética real</h3>
  <p>Una vivienda bien aislada puede reducir hasta un 40% su consumo de calefacción y refrigeración. En un contexto de tarifas al alza y mayor conciencia sobre el consumo energético doméstico, ese ahorro se vuelve un argumento decisivo para cualquier proyecto.</p>

  <h3>2. Sustentabilidad medible</h3>
  <p>Más del 80% del material proviene de papel descartado que, en su mayoría, terminaría en rellenos sanitarios. La energía requerida para producirlo es una fracción de la que demandan otros aislantes industriales. Y al ser biodegradable al final de su ciclo de vida, cierra el círculo.</p>

  <blockquote>"Aislar bien es la decisión de diseño más rentable que un proyecto puede tomar. Es lo único que sigue rindiendo durante toda la vida útil del edificio."</blockquote>

  <h3>3. Confort interior</h3>
  <p>Más allá del ahorro económico, una casa aislada se siente distinta. Las temperaturas se mantienen estables, no hay sensaciones de pared fría, el ruido exterior se reduce y la calidad del aire mejora porque se evita la condensación y el moho.</p>

  <img src="../assets/img/obra-08.jpg" alt="Detalle de aplicación" style="width:100%;height:auto;border-radius:6px;margin:32px 0">

  <h2>Cómo se elige el espesor adecuado</h2>
  <p>El espesor correcto depende de tres variables principales:</p>
  <ul>
    <li><strong>Zona climática:</strong> según la norma IRAM 11603, Argentina se divide en zonas bioclimáticas. Cada una tiene un valor mínimo recomendado de resistencia térmica.</li>
    <li><strong>Tipo de envolvente:</strong> no es lo mismo aislar un techo que un muro o un entrepiso. Cada elemento tiene exigencias distintas.</li>
    <li><strong>Sistema constructivo:</strong> en steel frame o wood frame, el espesor está limitado por la profundidad del montante. En mampostería tradicional, depende de la cámara de aire disponible.</li>
  </ul>

  <h2>Próximos pasos</h2>
  <p>Si estás evaluando aislar una obra (nueva o existente), el primer paso es siempre el mismo: <strong>diagnosticar bien</strong>. Saber qué construcción tenés, qué resultados esperás y qué presupuesto manejás. A partir de ahí, definimos qué solución (soplado o proyectado) es la indicada.</p>

  <p>Podés escribirnos para coordinar una visita o pedir una cotización inicial. La consulta no tiene costo y, generalmente, podemos darte un estimado en menos de 48 horas.</p>

  <div class="post-author">
    <div class="post-author-img">EM</div>
    <div>
      <div class="post-author-name">Equipo EMAT</div>
      <div class="post-author-bio">Especialistas en aislación con celulosa reciclada · Córdoba, Argentina</div>
    </div>
  </div>

  <div style="text-align:center;margin-top:48px">
    <a href="../index.html#presupuesto" class="btn btn-p">Cotizar mi proyecto</a>
  </div>
</article>
'''


# ───────────────────────────────────────────────────────────
# GENERAR ARCHIVOS
# ───────────────────────────────────────────────────────────
pages = [
    {
        "filename": "arquitectos.html",
        "title": "EMAT para arquitectos — documentación técnica y certificaciones | Aislación con celulosa",
        "description": "Soluciones de aislación térmica y acústica para arquitectos: fichas técnicas, ensayos, manuales de instalación y aporte a certificaciones LEED y EDGE.",
        "og_title": "EMAT para arquitectos — Aislación técnica con celulosa reciclada",
        "og_desc": "Documentación técnica, especificaciones para pliego, asesoramiento en obra y aporte a certificaciones de construcción sustentable.",
        "asset_prefix": "",
        "page_url": "arquitectos.html",
        "hero": page_hero(
            "Para arquitectos",
            "Soluciones técnicas con respaldo<br><span class='accent'>para tus proyectos</span>",
            "Especificá EMAT en tus obras: documentación técnica completa, ensayos certificados, asesoramiento en detalles constructivos y aporte directo a certificaciones LEED y EDGE.",
            cta_label="Solicitar fichas técnicas",
            cta_href="index.html#cont",
            cta2_label="Hablar con un técnico",
            cta2_href="index.html#cont",
            bg_image="assets/img/obra-15.jpg",
        ),
        "content": arquitectos_content,
    },
    {
        "filename": "constructoras.html",
        "title": "EMAT para constructoras — productividad y rendimiento en obra | Aislación a granel",
        "description": "Aislación con celulosa para constructoras: modalidad a granel, capacitación a instaladores, logística desde Córdoba y mejor rendimiento por jornada.",
        "og_title": "EMAT para constructoras — Productividad en obra con celulosa",
        "og_desc": "Modalidades a granel y llave en mano. Capacitación a instaladores. Cotizaciones por volumen.",
        "asset_prefix": "",
        "page_url": "constructoras.html",
        "hero": page_hero(
            "Para constructoras",
            "Productividad y rendimiento<br><span class='accent'>para tu obra</span>",
            "Aislación con celulosa de alto rendimiento, modalidad a granel para tu equipo o aplicación llave en mano. Capacitación técnica, logística confiable y mejores tiempos de obra.",
            cta_label="Cotizar por volumen",
            cta_href="index.html#cont",
            cta2_label="Coordinar visita técnica",
            cta2_href="index.html#cont",
            bg_image="assets/img/obra-08.jpg",
        ),
        "content": constructoras_content,
    },
    {
        "filename": "hogar.html",
        "title": "EMAT para tu hogar — más confort, menos consumo | Aislación con celulosa para casas",
        "description": "Aislación de celulosa reciclada para tu casa: confort todo el año, ahorro en gas y luz, menos ruido, mejor calidad del aire interior. Sin obras grandes.",
        "og_title": "EMAT para tu hogar — Confort y ahorro real con celulosa",
        "og_desc": "Aislás tu casa sin romper paredes. Hasta 40% menos consumo, mejor confort, más salud.",
        "asset_prefix": "",
        "page_url": "hogar.html",
        "hero": page_hero(
            "Para tu hogar",
            "Tu casa, más confortable<br><span class='accent'>y eficiente</span>",
            "Aislá tu hogar con celulosa reciclada y sentí la diferencia desde el primer día: temperatura estable todo el año, menos ruido, ahorro real en gas y luz, sin obras grandes.",
            cta_label="Cotizar para mi casa",
            cta_href="index.html#presupuesto",
            cta2_label="Pedir asesoramiento",
            cta2_href="index.html#cont",
            bg_image="assets/img/obra-02.jpg",
        ),
        "content": hogar_content,
    },
    {
        "filename": "quienes-somos.html",
        "title": "Quiénes somos — EMAT | Innovación en aislación sustentable con celulosa",
        "description": "EMAT: experiencia corporativa aplicada a una construcción más humana. Especialistas en aislación térmica y acústica con celulosa reciclada en Córdoba, Argentina.",
        "og_title": "Quiénes somos — EMAT",
        "og_desc": "El equipo, la historia y el propósito detrás de EMAT.",
        "asset_prefix": "",
        "page_url": "quienes-somos.html",
        "hero": page_hero(
            "Quiénes somos",
            "INNOVACIÓN EN<br><span class='accent'>AISLACIÓN</span><br><span class='soft'>sustentable con celulosa</span>",
            "Experiencia corporativa aplicada a una construcción más humana, eficiente y consciente con el medio ambiente.",
            cta_label="Conocernos",
            cta_href="#historia",
            cta2_label="Ir al contacto",
            cta2_href="index.html#cont",
            bg_image="assets/img/obra-05.jpg",
        ),
        "content": quienes_content,
    },
]

# Generar páginas en raíz
for page in pages:
    html = render_page(
        title=page["title"],
        description=page["description"],
        og_title=page["og_title"],
        og_desc=page["og_desc"],
        body_class=page.get("body_class",""),
        hero_html=page["hero"],
        content_html=page["content"],
        asset_prefix=page["asset_prefix"],
        page_url=page["page_url"],
    )
    out_path = os.path.join(BASE_DIR, page["filename"])
    with open(out_path,"w") as f: f.write(html)
    print(f"✓ {page['filename']} ({len(html)} chars)")

# Crear carpeta blog/
blog_dir = os.path.join(BASE_DIR, "blog")
os.makedirs(blog_dir, exist_ok=True)

# Blog index
blog_index_html = render_page(
    title="Blog EMAT — Aislación, eficiencia y construcción sustentable",
    description="Notas sobre aislación con celulosa, eficiencia energética, casos de obra y novedades del sector. Blog de EMAT, Córdoba.",
    og_title="Blog EMAT",
    og_desc="Notas sobre construcción sustentable, eficiencia energética y aislación con celulosa.",
    body_class="",
    hero_html=page_hero(
        "Blog",
        "Conocimiento sobre<br><span class='accent'>construcción sustentable</span>",
        "Notas, casos de obra, novedades técnicas y reflexiones sobre eficiencia energética, aislación y economía circular en la construcción.",
        cta_label="Cotizar un proyecto",
        cta_href="../index.html#presupuesto",
        bg_image="../assets/img/obra-13.jpg",
    ),
    content_html=blog_index_content,
    asset_prefix="../",
    page_url="blog/",
)
with open(os.path.join(blog_dir, "index.html"),"w") as f: f.write(blog_index_html)
print(f"✓ blog/index.html ({len(blog_index_html)} chars)")

# Blog post de ejemplo
post_html = render_page(
    title="Por qué la celulosa reciclada es el futuro de la aislación | Blog EMAT",
    description="Una mirada profunda a cómo el papel reciclado se convierte en uno de los aislantes más eficientes del mercado, con menor huella de carbono.",
    og_title="Por qué la celulosa reciclada es el futuro de la aislación",
    og_desc="El papel reciclado se transforma en uno de los aislantes más eficientes y sustentables del mercado.",
    body_class="",
    hero_html='''<section class="page-hero" style="min-height:auto;padding:130px 0 60px">
  <div class="page-hero-bg" style="background-image:linear-gradient(135deg,rgba(8,26,11,.75) 0%,rgba(16,46,22,.6) 50%,rgba(26,72,34,.55) 100%),url(\'../assets/img/obra-01.jpg\');background-size:cover;background-position:center"></div>
  <div class="wrap">
    <div class="hero-c sr" style="max-width:780px">
      <div class="post-meta"><span class="bp-cat">Sustentabilidad</span><span>29 Abril 2026</span><span>· 6 min de lectura</span></div>
      <h1 class="hero-h1 page-hero-h1" style="font-size:clamp(28px,4.2vw,46px)">Por qué la celulosa reciclada es el futuro de la aislación</h1>
    </div>
  </div>
</section>''',
    content_html=blog_post_content,
    asset_prefix="../",
    page_url="blog/post-ejemplo.html",
)
with open(os.path.join(blog_dir, "post-ejemplo.html"),"w") as f: f.write(post_html)
print(f"✓ blog/post-ejemplo.html ({len(post_html)} chars)")

print("\nPáginas generadas. Listas para abrir en el preview.")
