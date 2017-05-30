var React = require('react');
var NavLink = require('react-router-dom').NavLink;

var Nav = () => {
    return (
        <ul>
            <li>
                <NavLink to='/'>Home</NavLink>
            </li>
            <li>
                <NavLink to='/create_question'>Create Question</NavLink>
            </li>
            <li>
                <NavLink to='/answer_question'>Answer Question</NavLink>
            </li>
        </ul>
    )
}

module.exports = Nav;