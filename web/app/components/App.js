var React = require('react');
var ReactRouter = require('react-router-dom');
var Router = ReactRouter.BrowserRouter;
var Route = ReactRouter.Route;
var Switch = ReactRouter.Switch;
var Nav = require('./Nav');
var MultipleChoice = require('./MultipleChoice');
var CreateMultipleChoice = require('./CreateMultipleChoice');
var Home = require('./Home');

class App extends React.Component {
    render () {
        return (
            <Router>
                <div className='container'>
                    <Nav />
                    <Switch>
                        <Route exact path='/' component={Home} />
                        <Route exact path='/answer_question' component={MultipleChoice} />
                        <Route exact path='/create_question' component={CreateMultipleChoice} />
                        <Route render={() => { return <p>N'hi ha res aqui!</p>}} />
                    </Switch>
                </div>
            </Router>
        )
    }
}

module.exports = App;