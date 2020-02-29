import {h} from "hyperapp"
import {Section} from "./design.js";

export default (state) =>{
    return Section(
        h("div", {}, [
            state.results
                ? h("div", {class: "columns is-multiline"}, [
                    Navi(state),
                    Content(state),
                    h("h3", {class: "column is-size-3"}, `上位${state.aggregate.upper}%にいます`),
                    h("div", {class: "column is-full"}, [
                        h("div", {class: "colums is-multiline is-mobile"}, state.results.scores.map(s => ScoreView(s))),
                    ]),
                    h("h2", {class: "column is-size-3"}, `あなたのトータルスコアは${state.results.total_points}です！`)
                ])
                : h("div", {style: {"margin": "5vh auto"}, class: ["has-text-centered"]}, [
                    state.loading
                        ? h("p", {class: ["has-text-grey-lighter", "is-size-3"]}, "。。。けいさんちゅう")
                        : h("p", {class: ["has-text-grey-lighter", "is-size-3"]}, "結果をここに表示します")
                ])
        ])
    )
}

const ScoreView = (score) => {
    return (
        h("div", {class: ["column", "is-full"]}, [
            h("div", {class: "columns box is-multiline", style: {"margin-bottom": "1px"}}, [
                h("div", {class: "column is-full"}, [
                    h("h3", {class: "is-size-5"}, `${score.title}: ${score.total}点`)
                ]),
                h("div", {class: "column is-full"}, score.reasons.map(r => h("p", {}, `${r.point}pt.　・・・・${r.detail}`)))
            ])
        ])
    )
}

const Content = (state) => {
  return (
    h("div", {class: "content"}, [
      h("div", {class: state.data1 ? "active" : ""}, "ほげほげ1"),
      h("div", {class: state.data2 ? "active" : ""}, "ほげほげ2"),
      h("div", {class: state.data3 ? "active" : ""}, "ほげほげ3")
    ])
  )
}

const Navi = (state) => {
    return (
      h("div", {class: "tabs"}, [
        h("ul", {}, [
            h("li", {class: state.data1 ? "active" : ""}, [
              h("a", {onClick: switchToData1}, "data1")
            ]),
            h("li", {class: state.data2 ? "active" : ""}, [
              h("a", {onClick: switchToData2}, "data2")
            ]),
            h("li", {class: state.data3 ? "active" : ""}, [
              h("a", {onClick: switchToData3}, "data3")
            ])
        ])
      ])
    )
}


const switchToData1 = (state) => ({...state, data1: true, data2: false, data3: false})
const switchToData2 = (state) => ({...state, data1: false, data2: true, data3: false})
const switchToData3 = (state) => ({...state, data1: false, data2: false, data3: true})
