// scroll reveal
const io = new IntersectionObserver((entries) => {
    entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
}, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
document.querySelectorAll('.reveal').forEach(el => io.observe(el));

// pipeline node lighting: sweep in sync with the flowing signal
const nodes = Array.from(document.querySelectorAll('.pipe-nodes .node'));
const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
if (!reduce && nodes.length) {
    let i = 0;
    setInterval(() => {
        nodes.forEach(n => n.classList.remove('lit'));
        nodes[i].classList.add('lit');
        if (nodes[i + 1]) nodes[i + 1].classList.add('lit');
        i = (i + 1) % nodes.length;
    }, 3400 / nodes.length);
}

// contact form: works out-of-the-box via mailto, upgrades to inbox delivery
// once YOUR_FORM_ID is replaced with a real Formspree form id.
const cform = document.querySelector('.cform');
if (cform) {
    const status = cform.querySelector('.cform-status');
    const endpoint = cform.getAttribute('action');
    const setStatus = (msg, err) => { status.textContent = msg; status.classList.toggle('err', !!err); };
    cform.addEventListener('submit', async (e) => {
        e.preventDefault();
        const data = new FormData(cform);
        if (data.get('_gotcha')) return; // spam honeypot
        const name = (data.get('name') || '').toString();
        const email = (data.get('email') || '').toString();
        const message = (data.get('message') || '').toString();

        if (endpoint.includes('YOUR_FORM_ID')) {
            // not configured yet -> open the visitor's mail client, pre-filled
            const subject = encodeURIComponent('Portfolio enquiry from ' + name);
            const body = encodeURIComponent(message + '\n\n' + name + ' (' + email + ')');
            window.location.href = 'mailto:mahad.ehsan@gmail.com?subject=' + subject + '&body=' + body;
            setStatus('Opening your email app…');
            return;
        }
        setStatus('Sending…');
        try {
            const res = await fetch(endpoint, { method: 'POST', body: data, headers: { 'Accept': 'application/json' } });
            if (res.ok) { cform.reset(); setStatus("Thanks, I'll get back to you soon."); }
            else { setStatus('Something went wrong. Please email mahad.ehsan@gmail.com', true); }
        } catch (err) {
            setStatus('Something went wrong. Please email mahad.ehsan@gmail.com', true);
        }
    });
}

// theme toggle: respects saved preference, falls back to OS preference
const toggle = document.querySelector('.theme-toggle');
if (toggle) {
    const saved = localStorage.getItem('theme');
    if (saved === 'light' || (!saved && window.matchMedia('(prefers-color-scheme: light)').matches)) {
        document.documentElement.classList.add('light');
    }
    toggle.addEventListener('click', () => {
        document.documentElement.classList.toggle('light');
        const isLight = document.documentElement.classList.contains('light');
        localStorage.setItem('theme', isLight ? 'light' : 'dark');
    });
}