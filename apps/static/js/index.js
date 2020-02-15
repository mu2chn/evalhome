async function main(){
    const body = document.body
    evaluate()
}

async function evaluate(){
    const position = await getLocation()
    const results = await getData(position.latitude, position.longitude)
    
    document.body.appendChild(craeteResultsFragment(results))
}

function craeteResultsFragment(results){
    const total = results.total_points
    const scores = results.scores
    const fragmaent = document.createDocumentFragment()
    const title = document.createElement('div')
    title.innerHTML = `<h2>Total_Score${total}</h2>`
    fragmaent.appendChild(title)

    for(score of scores){
        fragmaent.appendChild(createScore(score))
    }
    return fragmaent
}

// priate
function createScore(score){
    const fragmaent = document.createElement('div')
    const title = document.createElement('div')
    title.innerHTML = `<h3>${score.title}<br/>: score=${score.total}</h3>`
    fragmaent.appendChild(title)

    for(reason of score.reasons){
        const div = document.createElement('div')
        div.innerHTML = `<p>${reason.point}pt.　・・・・${reason.detail}</p>`
        fragmaent.appendChild(div)
    }
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

main()