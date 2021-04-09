import React from 'react'
import USA from 'react-usa-map'

const Map = () => {

    const mapHandler = (e) => {
        alert(e.target.dataset.name)
    }


    return (
        <div>
            <USA onClick={(e) => mapHandler(e)}/> 
        </div>
    )
}

export default Map
