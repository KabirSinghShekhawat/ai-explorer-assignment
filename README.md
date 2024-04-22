# StackIt Hiring Assignment (AI Engineering Explorer)

### Welcome to StackIt's hiring assignment! 🚀

**If you didn't get here through github classroom, are you sure you're supposed to be here? 🤨**


We are glad to have you here, but before you read what you're going to beat your head over for the next few hours (maybe days?), let's get a few things straight:
- We really appreciate honesty. Don't copy anyone else's assignment, it'll only sabotage your chances
- You're free to use any stack, and library of your choice. Use whatever you can get your hands on, on the internet!
- We love out of the box solutions. We prefer to call it *Jugaad* 
- This might be just the first round, but carries the most importance of all. Give your best, and we hope you have a fun time solving this problem.

## ✨ **Software 2.0 is here, are you?** ✨

**Context**:
For any software company to integrate a 3rd party APIs (eg. Stripe APIs, Shopify APIs) they need to write integration code which often takes days/months to integrate across 20-30 CRUD use cases. It requires businesses to setup entire engineering teams, build data pipelines, hire product & project teams and what not. On top of that they need to manage code bases by handling errors that come time and again or upgrade whenever the API version changes.

**Today, YOU are going to make lives better for Engineering teams.**

**Assignment**:
Your task is to develop an AI Agent (RAG) that integrates the following READ APIs of Stripe without writing any custom code or fine-tuning a model. 
- https://docs.stripe.com/api/subscriptions/list
- https://docs.stripe.com/api/invoices/list
- https://docs.stripe.com/api/customers/list
- https://docs.stripe.com/api/refunds/list


**Typical Input & Output**:
Your end user is a software developer who will use your provided SDK to fetch data from Stripe account by providing an api key and the following information: 
1. Type of Data they want – Subscriptions / Invoices / Customers / Refunds (APIs listed above)
2. Filters & Sorts to apply
3. Limit of records they need to fetch.

Your output will be a json array of the record requested. 

**Other pointers**:
1. Do not custom code this out. Here is a bare minimum checklist (items) to handle – API schema, token security, filters & sort rules, datatypes.
2. Do not try to perfect it. It is a long journey. Build a proof of concept with decent degree of accuracy.
3. Brownie points if you can define proper benchmarks for such a tool's existence.
4. Pre reads
   - Software 2.0 by Andrej Karapathy – https://karpathy.medium.com/software-2-0-a64152b37c35
   - State of GPT – https://www.youtube.com/watch?v=bZQun8Y4L2A


**Evaluation criteria**:
1. Configurability of the integration
2. Software architecture
3. Accuracy/Reliability of the data obtained from the SDK.

## Submission ⏰
The timeline for this submission is: **Next 2 days**

Some things you might want to take care of:
- Make use of git and commit your steps!
- Use good coding practices.
- Write beautiful and readable code. Well-written code is nothing less than a work of art.
- Use semantic variable naming.
- Your code should be organized well in files and folders which is easy to figure out.
- If there is something happening in your code that is not very intuitive, add some comments.
- Add to this README at the bottom explaining your approach (brownie points 😋)

Once you're done, make sure you **record a video** showing your project working. The video should **NOT** be longer than 120 seconds. While you record the video, tell us about your biggest blocker, and how you overcame it! Don't be shy, talk us through, we'd love that.

We have a checklist at the bottom of this README file, which you should update as your progress with your assignment. It will help us evaluate your project.

- [ ✅ ] My code is somewhat working! 🥳
- [ ✅ ] I have recorded a video showing it working and embedded it in the README ▶️
- [ ] I have tested all the normal working cases 😎
- [ ] I have even solved some edge cases (brownie points) 💪
- [ ] I added my very planned-out approach to the problem at the end of this README 📜

## Got Questions❓
ASK Me if something is not clear. Whatsapp (9087858900) for instant reply or Email me (ad@nowstackit.com). Feel free to check the discussions tab, you might get something of help there. Check out that tab before reaching out to us. 
Also, did you know, the internet is a great place to explore? 😛

## Developer's Section
*Add your video here, and your approach to the problem (optional). Leave some comments for us here if you want, we will be reading this :)*


https://github.com/KabirSinghShekhawat/ai-explorer-assignment/assets/51289863/dee8d80e-50db-44b2-860b-327b544696bc

