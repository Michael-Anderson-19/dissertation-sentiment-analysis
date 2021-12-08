import React from 'react'; 

const Result = ({ resultData }) => {

    return (
        <div className="result-item">
            <p className="text"> {resultData.text}</p>
            <div className="prediciton-container">
                <p className="probability">{resultData.probability}</p>
                <p className="prediction">{resultData.prediction}</p>
            </div>
        </div>
    );
}

export default Result;