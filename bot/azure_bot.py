from botbuilder.core import ActivityHandler, MessageFactory, TurnContext
from botbuilder.schema import ChannelAccount, Activity, ActivityTypes
from adaptors.gpt import gpt_response


class AzureBot(ActivityHandler):
    async def on_members_added_activity(
        self, members_added: [ChannelAccount], turn_context: TurnContext
    ):
        for member in members_added:
            if member.id != turn_context.activity.recipient.id:
                await turn_context.send_activity("Hello and welcome!")

    async def on_message_activity(self, turn_context: TurnContext):
        if turn_context.activity.type == ActivityTypes.message: 
            await turn_context.send_activity(Activity(type=ActivityTypes.typing))
            user_input = turn_context.activity.text
            response =  gpt_response(user_input)
            return await turn_context.send_activity(
                MessageFactory.text(f"{response}"))