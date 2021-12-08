import React from 'react'; 

const MainResult = ({ mainPred,mainProb, isLoading, error }) => {

    if(error)
    {
        return (
            <div className="main-result">
                <div className="main-result-text">  
                    <p className="error-text results-header">an error occured {error}</p>
                </div>
            </div>
            );
    }

    if(isLoading)
    {
        return (
            <div className="main-result">
                <div className="main-result-text">  
                    <p className="loading-text results-header">making prediction...</p> 
                    <i class="fas fa-spinner loading-icon"></i>
                </div>
            </div>
            );
    }
   
    //if the mainPrediction and mainProbabilities are set and the isLoading and error states are not then show the results 
    if(mainPred && mainProb)
    {
      return(
        <div className="main-result">
            <div className="main-result-text">
                <p>The average sentiment of these tweets is <b>{mainPred}</b>{mainPred === "positive" ? ' 😃' : ' 🙁'}</p>
                <p>the breakdown of the tweets is <b>{mainProb}</b></p>
            </div>
        </div>
        );  
    }

    //initial empty state
    return (
        <div className="main-result">
            <div className="main-result-text">
                <p>Please enter a keyword or phrase to predict the polarity of tweets containing that specified keyword.</p>
                <p>The API will collect tweets created within the last 7 days that contain the keyword.</p>
                <p>The sentiment of these tweets will then be classified using the Sentiment analysis model and the results will be shown here.</p>
            </div>
        </div>
    )
    
}

export default MainResult;