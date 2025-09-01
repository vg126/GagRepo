---
title: "Quick Start"
sidebar_position: 2
description: |
  Canvas apps are interactive web applications hosted on Poe. Unlike chat-based bots, Canvas apps provide custom visual interfaces for any kind of interactive ...
---
# What are Canvas apps?

Canvas apps are interactive web applications hosted on Poe. Unlike chat-based bots, Canvas apps provide custom visual interfaces for any kind of interactive experience. They can interact with the Poe environment in various ways - including calling models on Poe and using their responses in the app - enabling creators to develop applications ranging from simple tools and games to advanced AI-powered experiences. And using the [App Creator](https://poe.com/App-Creator) bot, anyone can bring their ideas to life just by describing them - **no coding required**.

## Examples of Canvas apps

- Simple (non-AI-powered) tools or games
  - Example: [ColorPicker](https://poe.com/ColorPicker) - Pick any color from your images and instantly get its HEX and RGB values.

![Image](https://files.readme.io/428b947211facc198bdf4bc5409b77c1dbef3f5f9b2b6fdbc8987041362854b5-image.png)


- Custom interfaces for single AI models
  - Example: [MagicErase](https://poe.com/MagicErase) - Remove unwanted objects from images using AI! Powered by [Bria-Eraser](https://poe.com/Bria-Eraser).

![Image](https://files.readme.io/59e3b49fa783f44f84f534fe1d295ab7514423d9795d6ffb97f5ca1f24c9dfe1-image.png)


Advanced AI workflows involving multiple models

- Example: [Chibify](https://poe.com/Chibify) - Transform any image into 3D Chibi art! Powered by GPT-4o and FLUX Pro 1.1.

![Image](https://files.readme.io/3d05499a843ee9680dd68686bd58dec6a312a775d09ef1dbc751255981a9294a-image.png)


- Example: [MemeGenBattle](https://poe.com/MemeGenBattle) - Pit AI models against each other in a meme generation showdown!

![Image](https://files.readme.io/bac1478858ba2a6287d940b89995787de88eea25f66e0fd53c81440c02e243c7-image.png)


# Getting started

Let's walk through the process of creating your first Canvas app:

1. **Initial setup**

   1. Click on the “Create” button in the left sidebar or visit [poe.com/create_bot](https://poe.com/create_bot)
   2. Select "Canvas app" as the type

![Image](https://files.readme.io/a88f651e708ab6fcacb4ac6da36ace1fd9ecc79a6844c1cad6acb1db9026fc5c-image.png)


2. **Choose your creation method**
   1. Generate with a bot **(Recommended - the following steps assume choosing this option)**
      1. Chat with [App Creator](https://poe.com/App-Creator) and describe what you want to create
   2. Build manually
      1. Provide your own application code

![Image](https://files.readme.io/7cdfec0f2174922bfaab82a40f4a17fed271e7056eeea5628d572eacb405e0f0-image.png)


3. **Describe your idea to [App Creator](https://poe.com/App-Creator) and iterate as needed**
   1. Example: “Create an interactive color picker tool that allows users to upload their own images”
   2. Potential followups could be:
      1. “Add a smooth transition animation when an image is uploaded”
      2. “Show the history of chosen colors below the image”
      3. “Add a feature that uses an AI model to suggest complementary colors”
         1. or specifically e.g. “@GPT-4o-mini” instead of “an AI model”
4. **Publish your app on Poe**

   1. Click “Publish” in the Canvas to share your application with others

![Image](https://files.readme.io/f57ea9661360e30aba2263138eeb1071ff8c7494a0bf1b4a220fce187a86efa1-image.png)


5. **Editing your app**
   1. To edit your app after publishing, click “Edit app” in the overflow menu of your app
   2. Click “Edit with @App-Creator” to use App Creator to iterate on the app
   3. When you’re ready to publish the application again, click “Publish” in the Canvas to update your app.

![Image](https://files.readme.io/c572789057d96cf5b8f40e51130703f1838c559320b4f1139a3bb4fae3cd1b7d-image.png)


# Canvas app development UI

The Canvas app development environment has two key components:

![](https://files.readme.io/85fb11a63f0389ec674aa18f192e7a7a3fc990c8d66cee348214994ad19dc6cc-image.png)

1. **Chat Interface (left)**
   1. Chat with App Creator here to create and iterate on your application using natural language
2. **Canvas UI (right)**
   1. View and interact with the application you created using App Creator immediately
   2. The top tool bar and overflow menu provides several tools such as showing the console (for viewing error or logging messages), fullscreen mode, and minimizing the Canvas UI

![Image](https://files.readme.io/9ee14ca10249d9100bc8a02219c4f00630e71e1c1c0b2d49d7ca4d36d6e17742-image.png)


# Working effectively with App Creator

Think of App Creator as your personal developer who can:

- Understand natural language
- Implement features within seconds or minutes
- Provide immediate feedback
- Suggest improvements

To get the best results from App Creator, clear communication is key. Here are several examples of good requests and less effective requests:

- Good requests:
  - "Create a calculator with a modern design that can perform basic math operations"
  - "Add a dark mode toggle button in the top right corner"
  - "Make the submit button larger and match the header color"
  - “Use @FLUX-pro-1.1 instead of @FLUX-schnell”
- Less effective:
  - "Make it better" (too vague)
  - "Add all the usual calculator features" (too broad)
  - "Use JavaScript to handle clicks" (unnecessarily technical)

> 💡 Brainstorm with App Creator
> 
> You can ask App Creator to help you brainstorm or evaluate various ideas! Try asking questions like:
> 
> - "What features would make this app more useful?"
> - "What other ways could we display this data?"
> - "How could we make this interface more intuitive?"

# Integration with the Poe environment

Canvas apps can interact with the Poe environment via the [Poe Embed API](/docs/canvas-apps/poe-embed-api). They can:

- Trigger messages to Poe bots on behalf of the user
  - When doing this, the application can optionally open the Chat UI (if the user was in fullscreen Canvas view)
- Receive bot responses to those messages and use them in the application
  - These bot responses can be streamed back to the Canvas application without waiting for the entire response to be completed.

For example, a Canvas app could send a message to **@Claude-3.5-Sonnet** asking it to analyze an image, and then display that analysis within the application.

Any specific behavior - e.g. which bot to use, whether to open the chat, or whether to stream the bot response - can be specified in natural language to App Creator, which will then implement the desired behavior.

# Troubleshooting

## Describing issues

If you notice any issues in your application, you can generally fix them by describing the issue to App Creator. To get the best results, be as clear and specific as possible regarding the issue.

- **Bad example**: “It’s not working.”
- **Better example**: "After clicking submit, the form clears but I don't see any response from @Claude-3.5-Sonnet in the output area"

## Sharing console errors

If you see any errors in the application’s console (which can be opened in the Canvas overflow menu), you can copy and paste the exact error in a message to App Creator to ask it to fix the issue. For best results, describe the steps to reproduce the error, e.g. “When I click the submit button, I see this error: …”.

![Image](https://files.readme.io/9d0c72134c380a5aec69b1354129b33ae7aa90b535627943ac9152f19564eae8-image.png)


## Examining your application’s messages to bots

You can examine the messages that your application sends to bots by looking at the chat. This can help you identify any issues in e.g. prompting that you can ask App Creator to fix.

![Image](https://files.readme.io/84df372449487a9c0ad4745a91b6a045ed48873b66502e22a73f635e2d3f4468-image.png)

-----

Limitations
Client only

Canvas apps are single-file HTML applications. They cannot run server-side code. Apart from loading resources from CDNs (see Fetching external resources), they generally cannot connect to external servers.
No included database

Canvas apps do not have an included way to persist data. This will change in the future. If you have your own server that can persist data, a canvas app can connect to it after disabling the CSP (see Fetching external resources). Alternatively, you can read/write data by sending messages to a server bot that you control.
Light/dark mode

Light/dark mode always works on Chrome and Firefox. On Safari, the canvas app will inherit the light/dark mode setting of the operating system, not Poe.

On poe.com/settings there are 3 different color scheme options:

    Forced light mode
    Forced dark mode
    System (inherit color scheme of system)

This means if the user has selected Forced light mode, and the operating system is in dark mode, in Safari the Canvas embed will show up as dark mode.
Service Workers and Shared Workers

Service workers and Shared workers are not enabled.
Web Workers

Only web workers initialized using blob:// or data:// urls are enabled.
Webcam and microphone

Webcam and microphone access is disabled for canvas apps.
Local storage

Browser local storage APIs are disabled for canvas apps.
Clipboard

Canvas apps can write to the clipboard, but cannot read from the clipboard.
History API

Canvas apps cannot use the History API.
Links/navigation

Cross origin links (such as <a href="https://www.google.com">) will trigger a "Do you want to open this url?" confirmation. If the user confirms, the link will open in a new tab (example).

Same origin links (such as <a href="/about">) are not possible in canvas embeds.
File downloads

File download links are enabled.

Similar to standard HTML websites, a clickable download button can be created by rendering a link with the download attribute (<a href="blob:..." download="My image">Download Image</a>) (example).

If the source of the file to be downloaded is not in the trusted origins list, the download will trigger a “Do you want to open this url?” confirmation. If the user confirms, the url will be opened in a new tab.
Window APIs

Because the canvas iframe lacks the allow-modals permission, methods like alert(), confirm(), print(), and prompt() will not work. Calling these methods will result in an error message being logged to the browser console.
Fetching external resources

Canvas apps can load libraries/resources from a set of trusted origins such as cdnjs.cloudflare.com and cdn.jsdelivr.net.

View trusted origins

Canvas apps have strict security restrictions that prevent them from connecting with untrusted origins. If the canvas app tries to load an untrusted resource, the Allow untrusted external resources confirmation will show. If the user clicks Allow all, the canvas app will reload without the security restrictions, and will then be allowed to load any resource.

To avoid triggering the Allow untrusted external resources confirmation, we recommended only loading JavaScript libraries or CSS frameworks from a trusted origin.

Example: https://poe.com/CSPBannerExample
----------
Poe Embed API
Getting started

The Poe Embed API is automatically included in HTML applications running inside Poe. Visit poe.com/App-Creator to build a canvas app that uses the api.
Methods

Methods are accessible through the window.Poe global object.
sendUserMessage	Sends a message on behalf of the current user
sendUserMessage	Sends a message in the chat on behalf of the current user.
registerHandler	Registers a function to receive the results of sendUserMessage
window.Poe.sendUserMessage

Sends a message in the chat on behalf of the current user. In some cases it may throw a PoeEmbedAPIError. To see the results of the message, use the registerHandler method.

The current user will be charged for the cost of the sent messages and in some cases will be asked to authorize the costs. Try it with poe.com/EmbedAPIDebugger.


 sendUserMessage<Stream extends boolean>(
    /** The text to send.  In most cases this should start with `@BotName` */
    text: string,
    options?: {
      /** Files to include */
      attachments?: File[];
      /** Whether to invoke the handler with incomplete results as they are available or to only invoke it with the final complete result.  Each result contains all tokens so far. */
      stream?: Stream;
      /** Whether to open the chat on send. */
      openChat?: boolean;
      /** The registered name of the handler function to invoke with the results */
      handler?: string;
      /** Optional additional context to pass to the handler. */
      handlerContext?: HandlerContext;
    }
  ): Promise<
    { success: boolean}
  >;

window.Poe.registerHandler

Registers a callback function to the results of sendUserMessage. The callback receives results if the name of the handler, matches the handler argument passed into sendUserMessage.

  registerHandler(
    /**
     * String identifier for the handler. Used to associate responses with this callback.
     */
    name: string,
    /**
     * Callback function that receives response messages. Each result contains an array
     * of messages with their content and status.
     * The handlerContext specified in the sendUserMessage call will also be passed to the callback.
     */
    func: (result: SendUserMessageResult, context: HandlerContext) => void
  ): VoidFunction;

Example:

let someFile: File

window.Poe.registerHandler("myHandler", (result) => {
  console.log(result.responses[0]?.content)
})

let result = await window.Poe.sendUserMessage(
    "@assistant what is this?",
    { attachments: [someFile], stream: true, handler: "myHandler" }
 )
 console.log(result) // { success: true }

Objects
SendUserMessageResult

This object is passed into handlers of sendUserMessage calls.


type SendUserMessageResult = {
  status: "incomplete" | "complete" | "error";
  /**
   * In most cases, this will be a single bot message however in some cases a single human message
   * may trigger multiple bot responses.
   */
  responses: Message[];
};

Message

A message from a bot that may appear in SendUserMessageResult["responses"]. content always contains the text of the message so far.

/** A message from the bot. */
type Message = {
  messageId: string;
  /** The name of the bot that sent the message. e.g. "Assistant" */
  senderId: string;
  /** The entire content of the message recieved so far */
  content: string;
  /** Either text/plain or text/markdown */
  contentType: string;
  /** Each status should be handled to let the user know the current state of the message. */
  status: "incomplete" | "complete" | "error";
  /** A user friendly message to explain the current status.  Usually only specified for error status. */
  statusText?: string;
  attachments?: MessageAttachment[];
};

Errors
PoeEmbedAPIError

The error that may be thrown by sendUserMessage.

interface PoeEmbedAPIError extends Error {
  errorType: PoeEmbedAPIErrorType;
}

type PoeEmbedAPIErrorType = "UNKNOWN" | "INVALID_INPUT" | "USER_REJECTED_CONFIRMATION" | "ANOTHER_CONFIRMATION_IS_OPEN"

PoeApiErrorType is a union of strings:

    UNKNOWN - Something unexpected happened. This may occur when using an old version of the sdk
    INVALID_INPUT - When the input was invalid. Check error.message for more info
    USER_REJECTED_CONFIRMATION - When the action requires user confirmation, and the user rejected it
    ANOTHER_CONFIRMATION_IS_OPEN - When the action (e.g. sendUserMessage) requires user confirmation, but another confirmation is already open.
        This error is only relevant to “inline” codeblock previews that are rendered inside a message.

Typescript Definitions


/** The public interface of the Embed API.  This class is accessible from `window.Poe` */
interface PoeEmbedAPI {
  /** Send a message to the bot. */
  sendUserMessage<Stream extends boolean>(
    /** The text to send.  In most cases this should start with `@BotName` */
    text: string,
    options?: {
      /** Files to include in the user message. */
      attachments?: File[];
      /** Whether to invoke the handler with incomplete results as they are available or to only invoke it with the final complete result.  Each result contains all tokens so far. */
      stream?: Stream;
      /** Whether to open the chat on send. */
      openChat?: boolean;
      /** The name of the handler function to invoke with the results */
      handler?: string;
      /** Optional additional context to pass to the handler. */
      handlerContext?: HandlerContext;
    }
  ): Promise<
    { success: boolean}
  >;

  /** Register a handler function that is invoked with the results of the `sendUserMessage` call. The handler should be registered before the `sendUserMessage` call is made and ideally before the user has made interactions with the page. */
  registerHandler(
    /** The name of the handler function to register. This name should match the `handler` option in `sendUserMessage`. */
    name: string,
    /** The function that is invoked with the results of the `sendUserMessage` call. */
    func: (result: SendUserMessageResult, context: HandlerContext) => void
  ): VoidFunction;

  APIError: typeof PoeEmbedAPIError;
}

/** Error that may be thrown by an Embed API method such as `sendUserMessage` */
class PoeEmbedAPIError extends Error {
  errorType: PoeEmbedAPIErrorType;
}

type MessageAttachment = {
  attachmentId: string;
  mimeType: string;
  url: string;
  isInline: boolean;
  name: string;
};

/** A message from the bot. */
type Message = {
  messageId: string;
  /** The name of the bot that sent the message. e.g. "Assistant" */
  senderId: string;
  /** The entire content of the message recieved so far */
  content: string;
  /** Either text/plain or text/markdown */
  contentType: string;
  /** Each status should be handled to let the user know the current state of the message. */
  status: "incomplete" | "complete" | "error";
  /** A user friendly message to explain the current status.  Usually only specified for error status. */
  statusText?: string;
  attachments?: MessageAttachment[];
};

type SendUserMessageResult = {
  status: "incomplete" | "complete" | "error";
  /**
   * In most cases, this will be a single bot message however in some cases a single human message
   * may trigger multiple bot responses.
   */
  responses: Message[];
};

type HandlerContext = Record<string, any>;
type HandlerFunc = (
  result: SendUserMessageResult,
  context: HandlerContext
) => void;

type PoeEmbedAPIErrorType =
  | "UNKNOWN"
  | "INVALID_INPUT"
  | "USER_REJECTED_CONFIRMATION"
  | "ANOTHER_CONFIRMATION_IS_OPEN";

/** accessible via window.Poe */
declare global {
  interface Window {
    Poe: PoeEmbedAPI;
  }
}

