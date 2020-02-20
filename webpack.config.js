module.exports = {
    mode: 'development',
    entry: [ __dirname + "/front/entry.js"],
    output: {
        filename: 'bundle.js',
        path: __dirname + '/apps/static/js'
    },
    module: {
        rules: [
            {
                test: /\.scss$/,
                use: [
                    'style-loader',
                    'css-loader',
                    'sass-loader'
                ]
            },
        ]
    }
};
