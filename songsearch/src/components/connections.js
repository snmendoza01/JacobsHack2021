import axios from "axios";

function SongPOST(valueToSubmit, setReturnedValue) {
    axios
        .post("http://10.72.1.14:5000/search", { search: valueToSubmit })
        .then((response) => {
            setReturnedValue(response.data);
        })
        .catch((error) => {
            console.error("There was an error!", error);
        });
}

function PredictSongsPOST(ids, setResponseSongs) {
    axios
        .post("http://10.72.1.14:5000/predictSongs", {
            data: JSON.parse(JSON.stringify(ids)),
        })
        .then((response) => {
            console.log(response.data);
            setResponseSongs(response.data);
        })
        .catch((error) => {
            console.error("There was an error!", error);
        });
}

function SubmitRating(sliderValue) {
    console.log(sliderValue);
    // axios
    //     .post("http://10.72.1.14:5000/submitRating", {
    //         data: JSON.parse(JSON.stringify(ids)),
    //     })
    //     .then((response) => {
    //         console.log(response);
    //     })
    //     .catch((error) => {
    //         console.error("There was an error!", error);
    //     });
}

export { SongPOST, PredictSongsPOST, SubmitRating };
