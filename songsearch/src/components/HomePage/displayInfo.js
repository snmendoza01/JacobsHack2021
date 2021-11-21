import { motion } from "framer-motion";

export default function DisplayPrimaryInfo({ returnedValue, setIDs, ids }) {
    return (
        <table className="w-full m-auto border border-collapse border-gray-600 rounded-md table-fixed ">
            <tr>
                <th className="w-5/12 border border-gray-700 ">Artist</th>
                <th className="w-6/12 m-auto border border-gray-700 ">Track</th>
                <th className="w-1/12 border border-gray-700 ">
                    <svg
                        xmlns="http://www.w3.org/2000/svg"
                        className="block w-5 h-5 m-auto"
                        viewBox="0 0 20 20"
                        fill="currentColor"
                    >
                        <path d="M5 4a1 1 0 00-2 0v7.268a2 2 0 000 3.464V16a1 1 0 102 0v-1.268a2 2 0 000-3.464V4zM11 4a1 1 0 10-2 0v1.268a2 2 0 000 3.464V16a1 1 0 102 0V8.732a2 2 0 000-3.464V4zM16 3a1 1 0 011 1v7.268a2 2 0 010 3.464V16a1 1 0 11-2 0v-1.268a2 2 0 010-3.464V4a1 1 0 011-1z" />
                    </svg>
                </th>
            </tr>

            {Object.keys(returnedValue).map((elem, index) => {
                return (
                    <tr key={index}>
                        <td className="px-1 text-sm text-center truncate border border-gray-600">
                            {JSON.stringify(returnedValue[elem].artist).replace(
                                /(^"|"$)/g,
                                ""
                            )}
                        </td>
                        <td className="px-1 text-sm text-center truncate border border-gray-600">
                            {JSON.stringify(
                                returnedValue[elem].track_name
                            ).replace(/(^"|"$)/g, "")}
                        </td>

                        <td className="border border-gray-600 ">
                            {ids.includes(returnedValue[elem].track_id) ? (
                                <motion.svg
                                    whileTap={{ scale: 0.9 }}
                                    xmlns="http://www.w3.org/2000/svg"
                                    className="block w-5 h-5 m-auto text-red-600 dark:text-red-700"
                                    fill="none"
                                    viewBox="0 0 24 24"
                                    stroke="currentColor"
                                    onClick={() =>
                                        setIDs(
                                            ids.filter(
                                                (oldVals) =>
                                                    oldVals !==
                                                    returnedValue[elem].track_id
                                            )
                                        )
                                    }
                                >
                                    <path
                                        strokeLinecap="round"
                                        strokeLinejoin="round"
                                        strokeWidth={2}
                                        d="M6 18L18 6M6 6l12 12"
                                    />
                                </motion.svg>
                            ) : (
                                <motion.svg
                                    whileTap={{ scale: 0.9 }}
                                    xmlns="http://www.w3.org/2000/svg"
                                    className="block w-6 h-6 m-auto text-green-600 dark:text-green-600"
                                    fill="none"
                                    viewBox="0 0 24 24"
                                    stroke="currentColor"
                                    onClick={() =>
                                        setIDs((oldVals) => [
                                            ...oldVals,
                                            returnedValue[elem].track_id,
                                        ])
                                    }
                                >
                                    <path
                                        strokeLinecap="round"
                                        strokeLinejoin="round"
                                        strokeWidth={2}
                                        d="M12 4v16m8-8H4"
                                    />
                                </motion.svg>
                            )}
                        </td>
                    </tr>
                );
            })}
        </table>
    );
}
