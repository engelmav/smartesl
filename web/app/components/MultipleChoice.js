var React = require('react');
var PropTypes = require('prop-types');


class MultipleChoice extends React.Component {
    constructor (props) {
        super(props);

        this.state = {
            selectedAnswer: null
        }
    }

    handleChange(value) {
        this.setState( { selectedAnswer: value } )
    }

    render () {
        return (
            <div>
                <p>{this.props.question}</p>
                <form>
                    {this.props.choices.map(function(choice, idx) {
                        return (
                            <div key={idx}>
                                <label>
                                    <input type="radio" value={choice} />
                                    {choice}
                                </label>
                            </div>
                        )
                    })}
                </form>
            </div>
        )
    }
}

MultipleChoice.propTypes = {
    choices: PropTypes.array.isRequired,
    question: PropTypes.string.isRequired
}

MultipleChoice.defaultProps = {
    choices: [ "create", "created", "creating" ],
    question: "Twitter was _____ in March 2006 by Jack Dorsey, Evan Williams, Biz Stone and Noah Glass."
}

module.exports = MultipleChoice;
