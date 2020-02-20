import {app, h} from "hyperapp"

import {Container} from "../components/design.js"
import StartView from "../components/start.js"
import ResultView from "../components/result.js"

export default function(){
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
}