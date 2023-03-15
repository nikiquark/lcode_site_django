window.addEventListener('load', () => {
    const btns = document.querySelectorAll('.download__select__btn');
    const lin_guide = document.querySelector('.download__guide_linux');
    const win_guide = document.querySelector('.download__guide_windows')
    const lin_btn = document.querySelector('.download__select__btn_linux');
    const win_btn = document.querySelector('.download__select__btn_win')
    btns.forEach(btn => {
        btn.addEventListener('click', (e) => {
            const sys = e.target.dataset.system;
            if (sys === 'win') {
                lin_guide.classList.remove('download__guide_active');
                win_guide.classList.add('download__guide_active');
                win_btn.classList.add('download__select__btn_active');
                lin_btn.classList.remove('download__select__btn_active');
            }
            else if (sys === 'linux') {
                lin_guide.classList.add('download__guide_active');
                win_guide.classList.remove('download__guide_active');
                win_btn.classList.remove('download__select__btn_active');
                lin_btn.classList.add('download__select__btn_active');
                
            }
        })
    });
})