import React, { useState, useRef } from "react";
import { Avatar } from "@mui/material";
import useUserContext from "../../contexts/UserContext";
import usePostActionContext from "../../contexts/PostActionContext";
import usePageContext from "../../contexts/pageContext";

const ImagePreview = ({ file, removeImage }) => {
    return (
        <div className="w-full float-right relative mt-3">
            <img
                src={file}
                alt="selected file preview"
                className="w-full rounded-lg object-cover max-h-[60vh]"
            ></img>
            <button
                className="w-full h-full p-3  rounded-lg lg:text-2xl absolute top-0 left-0 bg-gray-900 opacity-0 hover:opacity-80 text-white transition-all"
                onClick={removeImage}
            >
                Remove Image
            </button>
        </div>
    );
};

const TweetForm = () => {
    const { setData } = usePageContext();
    const { createPost } = usePostActionContext();
    const [previewImage, setPreviewImage] = useState(true);
    const [file, setFile] = useState({ name: "", file: null });
    const {
        profileData: { username, profile_pic },
    } = useUserContext();
    const chooseImageFile = (e) => {
        e.preventDefault();
        document.querySelector("#post-image-field").click();
    };

    const fileInputRef = useRef();

    const submitForm = (e) => {
        e.preventDefault();
        const formElement = e.target;
        const success = (r) => {
            setData((prev) => {
                return { ...prev, posts: [r.data, ...prev.posts] };
            });
            formElement.content.value = "";
            formElement.image.value = "";
            setFile((prev) => ({ ...prev, file: null }));
        };
        createPost(new FormData(formElement), success, console.log);
    };

    const clearFile = (e) => {
        e.preventDefault();
        fileInputRef.value = null;
        setFile({
            name: "",
            file: null,
        });
    };

    React.useEffect(() => {
        const formElement = document.querySelector("#tweet-form");
        formElement.addEventListener("submit", submitForm);
        return () => {
            formElement.removeEventListener("submit", submitForm);
        };
    });
    return (
        <div className="w-[95%] max-w-[598px] grid-cols-[49px,_auto] h-min-content grid p-3  border-b-4 gap-1 bg-gray-100 mt-2 dark:bg-black dark:bg-opacity-90 dark:shadow-xl dark:border-gray-800">
            <div>
                <Avatar alt="post" src={profile_pic}>
                    {username && username.at(0).toUpperCase()}
                </Avatar>
            </div>
            <form
                className="flex flex-col gap-3 justify-between"
                action="/"
                method="post"
                id="tweet-form"
                encType="multipart/form-data"
            >
                <div>
                    <label htmlFor="main-tweet-form" className="fixed -top-[10000px]">
                        Post content
                    </label>
                    <input
                        type="text"
                        name="content"
                        id="main-tweet-form"
                        placeholder="Say Something?"
                        required
                        className="border-none p-2 text-[#5B7083] bg-white w-full  rounded-lg focus:outline-none text-sm dark:bg-gray-900 dark:text-gray-300"
                    />
                    <label htmlFor="post-image-field" className="fixed -top-[10000px]">
                        Select post image
                    </label>
                    <input
                        type="file"
                        accept="image/*"
                        name="image"
                        id="post-image-field"
                        className="fixed -top-[10000px]"
                        ref={fileInputRef}
                        onChange={(e) => {
                            const file = URL.createObjectURL(e.target.files[0]);
                            setFile({
                                file: file,
                                name: e.target.value.split("\\").pop(),
                            });
                        }}
                    />
                    <div className="text-gray-600 dark:text-gray-300 mt-2 pl-2">
                        Chosen File: {file.name}
                    </div>

                    {previewImage && file.file ? (
                        <ImagePreview file={file.file} removeImage={(e) => clearFile(e)} />
                    ) : null}
                </div>
                <div>
                    <button className="m-2 text-purple-500 text-2xl" onClick={chooseImageFile}>
                        <iconify-icon icon="bi:image">Choose Image</iconify-icon>
                    </button>
                    <button
                        className="m-2 text-purple-500 text-2xl"
                        onClick={(e) => {
                            e.preventDefault();
                            setPreviewImage((prev) => !prev);
                        }}
                    >
                        <iconify-icon
                            icon={
                                previewImage
                                    ? "ant-design:eye-invisible-filled"
                                    : "icon-park-outline:preview-open"
                            }
                        >
                            Toggle image preview
                        </iconify-icon>
                    </button>
                    <button className="bg-purple-400 text-purple-50 float-right px-2 h-8 rounded-full w-20">
                        Post
                    </button>
                </div>
            </form>
        </div>
    );
};

export default TweetForm;
