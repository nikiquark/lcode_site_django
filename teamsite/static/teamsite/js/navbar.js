window.addEventListener('load', ()=>{
    const btn = document.querySelector('.header__buttons__menu');
    const header_collapse = document.querySelector('.header');
    btn.addEventListener('click', ()=>{
        header_collapse.classList.toggle('header_collapse');
    })
    const settings_btn = document.querySelector('.header__buttons__setting');
    const settings =  document.querySelector('.header__setings');
    settings_btn.addEventListener('click', ()=>{
        settings.classList.toggle('header__setings_active');
    })
});