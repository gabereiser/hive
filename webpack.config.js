const path = require('path');
var webpack = require('webpack');

module.exports = {
  mode: 'production',
  entry: path.resolve(__dirname, 'hive/js/app.js'),
  output: {
    path: path.resolve(__dirname, 'hive/static/js'),
    filename: '[name].min.js'
  },
  plugins: [
    new webpack.ProvidePlugin({
      'React':     'react',
      'ReactDOM':  'react-dom',
      '$':         'jquery'
    })
  ],
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        loader: 'babel-loader',
        query: {
          presets: ['@babel/env', '@babel/react']
        }
      },
      { test: /\.css$/, use: 'css-loader' },
      { test: /\.scss$/, use: ['css-loader', 'sass-loader'] },
      {
        test: /\.(woff(2)?|ttf|eot|svg)(\?v=\d+\.\d+\.\d+)?$/,
        use: [
          {
            loader: 'file-loader',
            options: {
              name: '[name].[ext]',
              outputPath: '../fonts/'
            }
          }
        ]
      },
      {
        test: /\.(jpeg(2)?|jpg|gif|png)(\?v=\d+\.\d+\.\d+)?$/,
        use: [
          {
            loader: 'file-loader',
            options: {
              name: '[name].[ext]',
              outputPath: '../images/'
            }
          }
        ]
      }
    ]
  },
  resolve: {
    extensions: ['.js', '.json', '.jsx'] 
  }
};
