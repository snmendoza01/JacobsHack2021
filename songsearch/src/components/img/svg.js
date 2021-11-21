import { motion } from "framer-motion";

function MoonSVG() {
    return (
        <svg
            xmlns="http://www.w3.org/2000/svg"
            className="text-yellow-200 fill-current w-7 h-7 "
            viewBox="0 0 20 20"
            fill="currentColor"
        >
            <path d="M17.293 13.293A8 8 0 016.707 2.707a8.001 8.001 0 1010.586 10.586z" />
        </svg>
    );
}

function SunSVG() {
    return (
        <svg
            xmlns="http://www.w3.org/2000/svg"
            className="text-yellow-500 fill-current w-7 h-7 "
            viewBox="0 0 20 20"
            fill="currentColor"
        >
            <path
                fillRule="evenodd"
                d="M10 2a1 1 0 011 1v1a1 1 0 11-2 0V3a1 1 0 011-1zm4 8a4 4 0 11-8 0 4 4 0 018 0zm-.464 4.95l.707.707a1 1 0 001.414-1.414l-.707-.707a1 1 0 00-1.414 1.414zm2.12-10.607a1 1 0 010 1.414l-.706.707a1 1 0 11-1.414-1.414l.707-.707a1 1 0 011.414 0zM17 11a1 1 0 100-2h-1a1 1 0 100 2h1zm-7 4a1 1 0 011 1v1a1 1 0 11-2 0v-1a1 1 0 011-1zM5.05 6.464A1 1 0 106.465 5.05l-.708-.707a1 1 0 00-1.414 1.414l.707.707zm1.414 8.486l-.707.707a1 1 0 01-1.414-1.414l.707-.707a1 1 0 011.414 1.414zM4 11a1 1 0 100-2H3a1 1 0 000 2h1z"
                clipRule="evenodd"
            />
        </svg>
    );
}

function ArrowLeftSVG() {
    return (
        <motion.svg
            style={{ originX: "50%", originY: "50%" }}
            className="w-8 h-8 bg-gray-800 rounded-full ring-0 ring-offset-2 ring-offset-green-600"
            whileTap={{ scale: 0.9 }}
        ></motion.svg>
    );
}

function ArrowRightSVG() {
    return (
        <motion.svg
            style={{ originX: "50%", originY: "50%" }}
            className="w-8 h-8 bg-gray-200 rounded-full ring-0 ring-offset-2 ring-offset-green-500"
            whileTap={{ scale: 0.9 }}
        ></motion.svg>
    );
}

function SearchSVG() {
    return (
        <svg
            xmlns="http://www.w3.org/2000/svg"
            className="flex w-6 h-6 text-gray-400 dark:text-gray-300 "
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
        >
            <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth={2}
                d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
            />
        </svg>
    );
}

function BubbleBubbleToggleSVG({ setShowBubbles, showBubles }) {
    return showBubles ? (
        <svg
            key="bubblesvg1"
            xmlns="http://www.w3.org/2000/svg"
            className="w-8 h-8 text-gray-100 fill-current"
            viewBox="0 0 24 24"
            onClick={() => {
                setShowBubbles(!showBubles);
            }}
            fill="#000000"
        >
            <path d="M0 0h24v24H0V0z" fill="none" />
            <path d="M14.59 8L12 10.59 9.41 8 8 9.41 10.59 12 8 14.59 9.41 16 12 13.41 14.59 16 16 14.59 13.41 12 16 9.41 14.59 8zM12 2C6.47 2 2 6.47 2 12s4.47 10 10 10 10-4.47 10-10S17.53 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8z" />
        </svg>
    ) : (
        <svg
            key="bubblesvg2"
            xmlns="http://www.w3.org/2000/svg"
            className="w-8 h-8 text-gray-100 fill-current"
            viewBox="0 0 24 24"
            onClick={() => {
                setShowBubbles(!showBubles);
            }}
            fill="#000000"
        >
            <path d="M0 0h24v24H0V0z" fill="none" />
            <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.42 0-8-3.58-8-8s3.58-8 8-8 8 3.58 8 8-3.58 8-8 8z" />
        </svg>
    );
}

function Bubble({ width, height }) {
    function randomSpeed() {
        return Math.random() * (15 - 0 + 5) + 5;
    }

    function randomColor() {
        const rand = Math.floor(Math.random() * 6) + 1;
        return rand === 6 ? 50 : JSON.stringify(rand) + "00";
    }

    function repeatDelay() {
        return Math.random() * (2 - 0 + 1) + 0;
    }

    return (
        <div className="z-0 col-span-1">
            <motion.svg
                animate={{ y: -1000 }}
                initial={{ y: 1000 }}
                transition={{
                    repeat: Infinity,
                    repeatDelay: repeatDelay(),
                    duration: randomSpeed(),
                }}
                xmlns="http://www.w3.org/2000/svg"
                enableBackground="new 0 0 24 24"
                className={`absolute z-0 w-${width} h-${height} text-gray-${randomColor()} fill-current`}
                viewBox="0 0 24 24"
                fill="#000000"
            >
                <g>
                    <rect fill="none" height="24" width="24" />
                </g>
                <g>
                    <path d="M12,2C6.47,2,2,6.47,2,12c0,5.53,4.47,10,10,10s10-4.47,10-10C22,6.47,17.53,2,12,2z M12,20c-4.42,0-8-3.58-8-8 c0-4.42,3.58-8,8-8s8,3.58,8,8C20,16.42,16.42,20,12,20z" />
                </g>
            </motion.svg>
        </div>
    );
}

export {
    SearchSVG,
    SunSVG,
    MoonSVG,
    ArrowLeftSVG,
    ArrowRightSVG,
    Bubble,
    BubbleBubbleToggleSVG,
};
