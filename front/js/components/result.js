import {h} from "hyperapp"
import {Section} from "./design.js";

export default (state) =>{
    return Section(
        h("div", {}, [
            state.results
                ? h("div", {class: "columns is-multiline"}, [
                    h("div", {class: "column is-full"}, [
                        h("div", {class: "colums is-multiline"}, state.results.scores.map(s => ScoreView(s))),
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
        h("div", {class: ["column is-half"]}, [
            h("div", {class: "columns box is-vcentered is-multiline"}, [
                h("div", {class: "column is-full"}, [
                    h("h3", {class: "is-size-5"}, `${score.title}: ${score.total}点`)
                ]),
                h("div", {class: "column is-full"}, score.reasons.map(r => h("p", {}, `${r.point}pt.　・・・・${r.detail}`)))
            ])
        ])
    )
}