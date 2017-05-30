var React = require('react');
var PropTypes = require('prop-types');


class MultipleChoice extends React.Component {
    constructor (props) {
        super(props);

        this.state = {
            selectedAnswer: null
        }
        this.handleOptionChange = this.handleOptionChange.bind(this)
    }

    handleOptionChange(changeEvent) {
        console.log("Selected: " + changeEvent.target.value)
        this.setState( { selectedAnswer: changeEvent.target.value } )
    }

    render () {
        var answerButton = (choice, idx) => {
            return (
                <div key={idx}>
                    <label>
                        <input
                            type="radio"
                            value={choice}
                            checked={this.state.selectedAnswer === choice}
                            onChange={this.handleOptionChange} />
                            {choice}
                    </label>
                </div>
            )
        }
        return (
            <div>
                <p>{this.props.question}</p>
                <form>
                    {this.props.choices.map(answerButton)}
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
