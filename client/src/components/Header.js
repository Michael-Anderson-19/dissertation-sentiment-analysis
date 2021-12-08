import React from 'react';

const Header = ({ handleThemeChange }) => {

    return(
        <div className="header">
            <h1>Tweet Sentiment Analysis</h1>
            <button className="button" onClick={ ()=>handleThemeChange( (previousState) => { return !previousState} )} >Toggle Theme</button>
        </div>
    );
}

export default Header; 