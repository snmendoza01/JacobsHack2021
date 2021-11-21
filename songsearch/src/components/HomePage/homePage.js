import { motion } from "framer-motion";
import { useState } from "react";

import SearchBar from "./searchBar";
import DisplayPrimaryInfo from "./displayInfo";
import { PredictSongsPOST } from "../connections";
import { Bubble } from "../img/svg";
import RatingComponent from "./rating";
import FinalSong from "./finalSong";

export default function HomePage({ showBubles }) {
    const [searchValue, setSearchValue] = useState("");
    const [returnedValue, setReturnedValue] = useState([]);
    const [ids, setIDs] = useState([]);
    const [responceSongs, setResponseSongs] = useState({});

    const array = Array(20).fill(true);

    return (
        <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
        >
            <div className="flex min-h-screen subpixel-antialiased ">
                <div className="relative px-3 mt-20">
                    <div className="z-40 px-2 pt-5 pb-2 mb-10 bg-gray-300 rounded-lg shadow-xl ring-2 ring-gray-500 dark:bg-gray-700 dark:ring-gray-500 ring-opacity-80">
                        <SearchBar
                            key="searchBar"
                            searchValue={searchValue}
                            setSearchValue={setSearchValue}
                            setReturnedValue={setReturnedValue}
                        />
                    </div>

                    {returnedValue.length > 0 ? (
                        <motion.div
                            className="space-y-2"
                            animate={{ opacity: 1 }}
                            initial={{ opacity: 0 }}
                        >
                            <DisplayPrimaryInfo
                                key="primaryInfo"
                                returnedValue={returnedValue}
                                setIDs={setIDs}
                                ids={ids}
                            />

                            <div className="flex justify-center">
                                <motion.button
                                    whileTap={{ scale: 0.95 }}
                                    className="w-2/3 px-1 text-gray-200 bg-green-500 rounded-md dark:bg-green-600 dark:opacity-90"
                                    onClick={() =>
                                        PredictSongsPOST(ids, setResponseSongs)
                                    }
                                >
                                    Go
                                </motion.button>
                            </div>
                        </motion.div>
                    ) : (
                        <></>
                    )}
                    {Object.keys(responceSongs).length !== 0 ? (
                        <FinalSong responceSongs={responceSongs} />
                    ) : (
                        <></>
                    )}
                    {Object.keys(responceSongs).length !== 0 ? (
                        <RatingComponent />
                    ) : (
                        <></>
                    )}
                </div>
            </div>
            {showBubles ? (
                <div className="grid h-16 grid-cols-12 ">
                    {array.map((element, index) => {
                        return <Bubble key={index} width={6} height={6} />;
                    })}
                </div>
            ) : (
                <></>
            )}
        </motion.div>
    );
}
