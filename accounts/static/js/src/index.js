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

async function formatTipoProdutor(){
    const tipoProdutorField = document.getElementById('tipo-produtor')
    const TIPO_PRODUTOR = {
        "P" : "Produtor",
        "C" : "Comerciante",
        "F" : "Feira Orgânica"
    }
    let tipoProdutor = String(tipoProdutorField.innerHTML)
    tipoProdutorField.innerHTML = `Tipo: ${TIPO_PRODUTOR[tipoProdutor[tipoProdutor.length - 1]]}`

}
formatTipoProdutor();
addDropDown();