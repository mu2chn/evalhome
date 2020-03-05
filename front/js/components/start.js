import {h} from "hyperapp"
import {Section} from "./design.js";
import axios from "axios"

export default (state) => {
    return Section(
        h("div", {class: "has-text-centered"}, [
            h("div", {class: ["columns is-centered"]}, [
                h("div", {class: ["column is-half"]}, "自身の下宿が他人から見てどれくらい立地が良いのか調べることができます。以下のボタンを押して検索してみましょう。"),
            ]),
            h("button", {class: "button is-info", onClick: [evaluateAction], disabled: state.loading ? "yes": null}, "査定する")
        ])
    )
}

const evaluateAction = (state) => [
    {...state, results: null, loading: true},
    [
        async function(dispatch, {action}){
            const position = await getLocation()
            const results = await getData(position.latitude, position.longitude)
            dispatch(action, results)
        },
        {action: (state, results)=>({...state, results: results.scores, loading: false, aggregate: results.aggregate})}
    ]
]

function getData(lat, lng){
    return axios.get('/eval',{
        params: {
          lat: lat,
          lng: lng
        }
      })
        .then(res => {
            const results = res.data
            return results
        })
        .catch(reason => console.log("Cause Err"))
}

function getLocation(){
    return new Promise((resolve, reject)=> {
        // HTTPSでしか動作しない
        navigator.geolocation.getCurrentPosition(
            ((positon) => {
                // resolve(positon.coords)
                resolve({latitude: 35.041029, longitude: 135.782641})
            }),
            ((err) => {
                resolve({latitude: 35.041029, longitude: 135.782641})
                console.log("Cannot get location info")
            })
        );
    })
}
