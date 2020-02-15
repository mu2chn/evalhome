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
    state,
    [
        async function(dispatch, {action}){
            dispatch((state)=>({...state, results: null}))
            dispatch((state)=>({...state, loading: true}))
            const position = await getLocation()
            const results = await getData(position.latitude, position.longitude)
            dispatch(action, results)
            dispatch((state)=>({...state, loading: false}))
        },
        {action: (state, results)=>({...state, results: results})}
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
        h("div", {}, [
            h("p", {}, "京大生の住まいをランク付け！"),
            h("button", {class: "button is-primary", onClick: [evaluateAction], disabled: state.loading ? "yes": null}, "査定する")
        ])
    )
}

const ResultView = (state) =>{
    return Section(
        h("div", {}, [
            state.results
            ? h("div", {}, [
                h("div", {}, state.results.scores.map(s => ScoreView(s))),
                h("h2", {class: "is-size-3"}, `あなたのトータルスコアは${state.results.total_points}です！`)
            ])
            : state.loading
                ? h("p", {}, "。。。取得中です")
                : h("p", {}, "結果をここに表示します")
        ])
    )
}
const ScoreView = (score) => {
    return h("div", {}, [
        h("div", {}, [
            h("h3", {class: "is-size-5"}, `${score.title}: ${score.total}点`)
        ]),
        h("ol", {}, score.reasons.map(r => h("li", {}, `${r.point}pt.　・・・・${r.detail}`)))
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