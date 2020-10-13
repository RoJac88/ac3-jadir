const showFormButton = document.querySelector('#show-form')
const formWrap = document.querySelector('.form--wrap')
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
  formWrap.style.display = 'block'
  formWrap.style.transform = 'translateY(200px)'
  backdrop.addEventListener('click', () => {
    formWrap.style.transform = 'translateY(-380px)'
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

  const ra = form.get('ra')
  XHR.open( "PUT", "/alunos/" + ra )
  XHR.send(form)
}
