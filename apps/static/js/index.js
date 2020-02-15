async function evaluate(){
    const position = await getLocation()
    const results = await getData(position.latitude, position.longitude)
    document.getElementById("result").append(craeteResultsFragment(results))
}

function craeteResultsFragment(results){
    const total = results.total_points
    const scores = results.scores
    const fragmaent = document.createDocumentFragment()
    const title = document.createElement('div')
    title.innerHTML = `<h2 class="is-size-3">あなたのトータルスコアは${total}です！</h2>`

    for(score of scores){
        fragmaent.appendChild(createScore(score))
    }
    fragmaent.appendChild(title)
    return fragmaent
}

// priate
function createScore(score){
    const fragmaent = document.createElement('div')
    const title = document.createElement('div')
    title.innerHTML = `<h3 class="is-size-5">${score.title}: ${score.total}点</h3>`
    fragmaent.appendChild(title)
    const ol = document.createElement('ol')
    for(reason of score.reasons){
        const div = document.createElement('li')
        div.innerHTML = `${reason.point}pt.　・・・・${reason.detail}`
        ol.appendChild(div)
    }
    fragmaent.appendChild(ol)
    return fragmaent
}

function getData(lat, lng){
    return axios.get('/eval',{
        params: {
          lat: lat,
          lng: lng
        }
      })
        .then(res => {
            results = res.data
            return results
        })
        .catch(reason => console.log("Cause Err"))
}

function getLocation(){
    return new Promise((resolve, reject)=> {
        navigator.geolocation.getCurrentPosition(((positon) => {
            resolve(positon.coords)
        }), (err) => {
            // reject(err)
            resolve({latitude: 35.041058, longitude: 135.782566})
            console.log("Cannot get location info");
        });
    })
}

function main(){
    const body = document.body
    const buttton = document.getElementById("evaluate")
    buttton.addEventListener("click", evaluate, false)
}

window.addEventListener("load", main)