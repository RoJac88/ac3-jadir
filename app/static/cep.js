const cepInput = document.querySelector('input[name="cep"]')
cepInput.addEventListener('input', () => {
  const cepDigits = cepInput.value.replace('-', '')
  const cepIsDigits = /^\d+$/.test(cepDigits)
  if (cepIsDigits && cepDigits.length === 8) {
    const uri = `https://viacep.com.br/ws/${cepDigits}/json/`
    fetch(uri)
    .then(response => response.json())
    .then(data => {
      document.querySelector('input[name="log"]').value = data.logradouro
      document.querySelector('input[name="comp"]').value = data.complemento
    })
    .catch((error) => {
      console.log('Erro ao buscar CEP:', error)
    })
  }
})
