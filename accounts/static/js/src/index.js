async function addDropDown(){
    const dropdown = document.getElementById('user-dropdown');
    const userIcon = document.getElementById('User');

    userIcon.addEventListener('click', () => {
        if(dropdown.classList.contains('U-open')){
            dropdown.classList.remove('U-open')
        }else{
            dropdown.classList.add('U-open')
        }
    })
}

addDropDown();