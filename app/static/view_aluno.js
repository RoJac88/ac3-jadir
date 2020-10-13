const deleteButton = document.querySelector('.btn--delete')
deleteButton.addEventListener('click', () => {
  const XHR = new XMLHttpRequest()
  XHR.addEventListener( "load", function() {
    console.log(XMLHttpRequest)
    document.location.href="/alunos/"
  })
  let prompt = confirm('Deseja mesmo apagar este aluno?')
  if (prompt) {
    XHR.open('DELETE', deleteButton.dataset.href, true)
    XHR.send()
  }
})
