const MiniCssExtractPlugin = require("mini-css-extract-plugin");

module.exports = {
    mode: 'development',
    entry: [ __dirname + "/front/entry.js"],
    output: {
        filename: 'bundle.js',
        path: __dirname + '/apps/static'
    },
    module: {
        rules: [
            {
                test: /\.scss$/,
                use: [
                    MiniCssExtractPlugin.loader,
                    'css-loader',
                    'sass-loader'
                ]
            },
        ]
    },
    plugins: [
        new MiniCssExtractPlugin({
          filename: 'style.css'
        })
      ]
};