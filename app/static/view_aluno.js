
const showFormButton = document.querySelector('.btn--edit')
const formWrap = document.querySelector('.form--wrap')
formWrap.style.transition = 'transform 200ms ease-in'
formWrap.style.display = 'block'
const sendFormButton = document.querySelector('#submit')

sendFormButton.addEventListener('click', sendForm)
showFormButton.addEventListener('click', showForm)
formWrap.addEventListener('click', (e) => {
  e.stopPropagation()
})


function showForm() {
  const backdrop = document.querySelector('.form--backdrop')
  backdrop.style.pointerEvents = 'auto'
  backdrop.style.backgroundColor = 'rgba(0,0,0, 0.8)'
  formWrap.style.transform = 'translateY(200px)'
  backdrop.addEventListener('click', () => {
    formWrap.style.transform = 'translateY(-360px)'
    backdrop.style.pointerEvents = 'none'
    backdrop.style.backgroundColor = 'transparent'
  })
}


function sendForm() {
  const form = new FormData(document.querySelector('form'))
  const XHR = new XMLHttpRequest()

  XHR.addEventListener( "load", function() {
    location.reload()
  })
  const ra = document.querySelector('input[name="ra"]').value
  XHR.open( 'PATCH', location.href)
  XHR.send(form)
}


const deleteButton = document.querySelector('.btn--delete')
deleteButton.addEventListener('click', () => {
  const XHR = new XMLHttpRequest()
  XHR.addEventListener( "load", function() {
    console.log(XMLHttpRequest)
    document.location.href="/alunos/"
  })
  let prompt = confirm('Deseja mesmo apagar este aluno?')
  if (prompt) {
    XHR.open('DELETE', location.href)
    XHR.send()
  }
})


