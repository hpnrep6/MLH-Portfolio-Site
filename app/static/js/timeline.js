let form = document.querySelector('#timeline-form')
let timeline = document.querySelector('#timeline-posts')

function refreshTimeline() {
  fetch('/api/timeline_post', {
    method: 'GET'
  }).then( res => res.json() )
  .then( (data) => {
    timeline.innerHTML = ''
    console.log(data)
    for (let element of data['timeline_posts']) {
      timeline.innerHTML += `
        <div> 
          <div class='timeline-elem'>
            <div> Name: ${element.name} </div>
            <div> Email: ${element.email} </div>
            <div> Date: ${element.created_at} </div>
            <div> Content: ${element.content} </div>
          </div>

        </div>
      `
      console.log(element)
    }
  })
}

form.addEventListener('submit', (e) => {
  e.preventDefault()
  let formData = new FormData(form)

  // For some reason, the raw formData derived from the form does not work
  let f = new FormData()
  for (let key of formData.keys()) {
    f.append(key, formData.get(key))
  }

  fetch('/api/timeline_post', {
    body: f,
    method: 'POST'
  }).then((res) => {
    form.reset()
    refreshTimeline()
  }).catch((err) => {
    console.log(err)
  })
})

refreshTimeline()