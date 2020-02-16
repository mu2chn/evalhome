import { h, app } from "/js/hyperapp.js"

app({
    node: document.getElementById("app"),
    view: (state) => Container([
        StartView(state),
        ResultView(state)
    ]),
    init: {
        results: null,
        loading: false
    }
})

const evaluateAction = (state) => [
    {...state, results: null, loading: true},
    [
        async function(dispatch, {action}){
            const position = await getLocation()
            const results = await getData(position.latitude, position.longitude)
            dispatch(action, results)
        },
        {action: (state, results)=>({...state, results: results, loading: false})}
    ]
]

const Container = (contents) => h("div", {}, contents)

const Section = (content) => {
    return h("section", {class: "section"}, [
        h("div", {class: "container"}, [content])
    ])
}

const StartView = (state) => {
    return Section(
        h("div", {class: "has-text-centered"}, [
            h("div", {class: ["columns is-centered"]}, [
                h("div", {class: ["column is-half"]}, "自身の下宿が他人から見てどれくらい立地が良いのか調べることができます。以下のボタンを押して検索してみましょう。"),
            ]),
            h("button", {class: "button is-info", onClick: [evaluateAction], disabled: state.loading ? "yes": null}, "査定する")
        ])
    )
}

const ResultView = (state) =>{
    return Section(
        h("div", {}, [
            state.results
                ? h("div", {class: "columns is-multiline"}, [
                    h("div", {class: "column is-full"}, state.results.scores.map(s => ScoreView(s))),
                    h("h2", {class: "column is-size-3"}, `あなたのトータルスコアは${state.results.total_points}です！`)
                ])
                : h("div", {style: {"margin": "15vh auto"}, class: ["has-text-centered"]}, [
                    state.loading
                        ? h("p", {class: ["has-text-grey-lighter", "is-size-3"]}, "。。。けいさんちゅう")
                        : h("p", {class: ["has-text-grey-lighter", "is-size-3"]}, "結果をここに表示します")
                ])
        ])
    )
}
const ScoreView = (score) => {
    return h("div", {class: "columns box is-vcentered"}, [
        h("div", {class: "column is-half"}, [
            h("h3", {class: "is-size-5"}, `${score.title}: ${score.total}点`)
        ]),
        h("div", {class: "column is-half"}, score.reasons.map(r => h("p", {}, `${r.point}pt.　・・・・${r.detail}`)))
    ])
}

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
        navigator.geolocation.getCurrentPosition(((positon) => {
            resolve(positon.coords)
        }), (err) => {
            // reject(err)
            resolve({latitude: 35.024731, longitude: 135.797286})
            console.log("Cannot get location info");
        });
    })
}

function main(){}

window.addEventListener("load", main)