import React from 'react';
import Result from './Result'

const ResultsList = ({tweetPredicitons}) => {

    if(Object.keys(tweetPredicitons).length <= 0){
        return ""; 
    }

    return (
        <div className="results-list">
            {
                tweetPredicitons.map( (result) => <Result resultData={result}/>)
            }
        </div>
    )
}
export default ResultsList;