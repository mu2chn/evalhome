const body = document.body

function getData(lat, lng){
    axios.get('/eval')
        .then(res => {
            console.log(res)
        })
}