const path = require('path');
var webpack = require('webpack');

module.exports = {
  mode: 'development',
  entry: {
    app: path.resolve(__dirname, 'hive/js/app.jsx'),
    login_view: path.resolve(__dirname, 'hive/js/views/accounts/login.jsx'),
  },
  output: {
    path: path.resolve(__dirname, 'hive/static/js'),
    filename: '[name].min.js'
  },
  plugins: [
    new webpack.ProvidePlugin({
      'React':     'react',
      'ReactDOM':  'react-dom'
    })
  ],
  externals: {
    jquery: 'jQuery'
  },
  module: {
    rules: [
      {
        test: /\.(js|json|jsx)$/,
        exclude: /node_modules/,
        loader: 'babel-loader',
        query: {
          presets: ['@babel/env', '@babel/react']
        }
      },
      { test: /\.css$/, use: 'css-loader' },
      { test: /\.scss$/, use: ['css-loader', {
            loader: 'sass-loader',
            options: {
              name: '[name].[ext]',
              outputPath: '../css/'
            }
          }
        ] 
      },
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
        test: /\.(jpe?g|gif|png)(\?v=\d+\.\d+\.\d+)?$/,
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
