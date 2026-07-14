document.getElementById('nav-toggle')?.addEventListener('click', () => {
  const mobile = document.getElementById('nav-mobile');
  const menuIcon = document.getElementById('icon-menu');
  const closeIcon = document.getElementById('icon-close');
  const open = mobile.classList.toggle('open');
  document.body.classList.toggle('menu-open', open);
  menuIcon.style.display = open ? 'none' : 'block';
  closeIcon.style.display = open ? 'block' : 'none';
});

document.querySelectorAll('.step-tab').forEach(btn => {
  btn.addEventListener('click', () => {
    const id = btn.dataset.step;
    document.getElementById('step-' + id)?.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
  });
});
