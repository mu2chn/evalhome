import {h} from "hyperapp"

export const Container = (contents) => {
    return h("div", {}, contents)
}

export const Section = (content) => {
    return (
        h("section", {class: "section"}, [
            h("div", {class: "container"}, [content])
        ])
    )
}