import React from 'react';
const Input = ({ textValue, handleTextInput, clearText, makePrediciton, disable }) => {

    const InputTextHandler = (e) => {
        const text = e.target.value;
        handleTextInput(text);
        console.log(textValue)
    }
    
    return(
        <div className="input-section"> 
            <div className="input-container">
                <textarea value={textValue} onChange={InputTextHandler} placeholder="Enter a keyword or phrase..." > </textarea>
                <div className="input-button-container">
                    <button className="input-button clear-button" onClick={clearText} disabled={disable}>Clear</button>
                    <button className="input-button predict-button" onClick={makePrediciton} disabled={disable}>Predict</button>
                </div>
            </div>
        </div>
    )
}
export default Input;