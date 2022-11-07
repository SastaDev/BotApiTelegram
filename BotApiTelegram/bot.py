from . import types, methods

class Bot:
    def __init__(self):
        pass

    def get_me(self):
        return methods.getMe(self.bot).get_me()

    def send_message(self, chat_id, text, message_thread_id=None, parse_mode=None, entities=None, link_preview=None, disable_web_page_preview=None, disable_notification=None, protect_content=None, reply_to=None, reply_to_message_id=None, allow_sending_without_reply=None, buttons=None, reply_markup=None, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.id
        elif isinstance(chat_id, types.User):
            _chat_id = chat_id.user_id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.id
        else:
            _chat_id = chat_id
        if not parse_mode:
            parse_mode = self.default_settings.parse_mode
        if link_preview:
            disable_web_page_preview = link_preview
        elif disable_web_page_preview:
            pass
        else:
            disable_web_page_preview = self.default_settings.link_preview
        if reply_to:
            reply_to_message_id = reply_to
        if buttons:
            reply_markup = buttons
        msg = methods.sendMessage(bot=self.bot, chat_id=_chat_id, text=text, message_thread_id=message_thread_id, parse_mode=parse_mode, entities=entities, disable_notification=disable_notification, protect_content=protect_content, reply_to_message_id=reply_to_message_id, reply_markup=reply_markup, **kwargs).send_message()
        return types.Message_(bot=self.bot, msg=msg)

    def delete_message(self, chat_id, message_id, *args, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.id
        elif isinstance(chat_id, types.User):
            _chat_id = chat_id.user_id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.id
        else:
            _chat_id = chat_id
        if isinstance(message_id, list):
            success = []
            for msg_id in message_id:
                d = methods.deleteMessage(bot=self.bot, chat_id=_chat_id, message_id=msg_id).delete_message()
                success.append(d)
            return d
        else:
            return methods.deleteMessage(bot=self.bot, chat_id=_chat_id, message_id=message_id, *args, **kwargs).delete_message()

    def forward_message(self, chat_id, from_chat_id, message_id, message_thread_id=None, disable_notification=None, protect_content=None, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.id
        else:
            _chat_id = chat_id
        if isinstance(message_id, (types.Message, types.Message_, types.MessageId)):
            _message_id = message_id.message_id
        else:
            _message_id = message_id
        return methods.forwardMessage(bot=self.bot, chat_id=_chat_id, message_thread_id=message_thread_id, disable_notification=disable_notification, protect_content=protect_content, message_id=_message_id).forward_message()

    def copy_message(self, chat_id, from_chat_id, message_id, message_thread_id=None, caption=None, parse_mode=None, caption_entities=None, disable_notification=None, protect_content=None, reply_to=None, reply_to_message_id=None, allow_sending_without_reply=None, buttons=None, reply_markup=None, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.id
        elif isinstance(chat_id, types.User):
            _chat_id = chat_id.user_id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.id
        else:
            _chat_id = chat_id
        if isinstance(from_chat_id, types.Chat):
            _from_chat_id = from_chat_id.id
        elif isinstance(chat_id, types.User):
            _from_chat_id = from_chat_id.user_id
        elif isinstance(from_chat_id, types.Message):
            _from_chat_id = from_chat_id.chat.id
        else:
            _from_chat_id = from_chat_id
        if isinstance(message_id, (types.Message, types.Message_, types.MessageId)):
            _message_id = message_id.message_id
        else:
            _message_id = message_id
        if reply_to:
            reply_to_message_id = reply_to
        if buttons:
            reply_markup = buttons
        return methods.copyMessage(bot=self.bot, chat_id=_chat_id, from_chat_id=_from_chat_id, message_id=_message_id, message_thread_id=message_thread_id, caption=caption, parse_mode=parse_mode, caption_entities=caption_entities, disable_notification=disable_notification, protect_content=protect_content, reply_to_message_id=reply_to_message_id, allow_sending_without_reply=allow_sending_without_reply, reply_markup=reply_markup, **kwargs)

    def send_photo(self, chat_id, photo, message_thread_id=None, caption=None, parse_mode=None, caption_entities=None, disable_notification=False, protect_content=False, reply_to=None, reply_to_message_id=None, allow_sending_without_reply=None, buttons=None, reply_markup=None, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.id
        else:
            _chat_id = chat_id
        if not parse_mode:
            parse_mode = self.default_settings.parse_mode
        if link_preview:
            disable_web_page_preview = link_preview
        elif disable_web_page_preview:
            pass
        else:
            disable_web_page_preview = self.default_settings.link_preview 
        if reply_to:
            reply_to_message_id = reply_to
        if buttons:
            reply_markup = buttons
        msg = methods.sendPhoto(bot=self.bot, chat_id=_chat_id, photo=photo, message_thread_id=message_thread_id, caption=caption, parse_mode=parse_mode, caption_entities=caption_entities, disable_notification=disable_notification, protect_content=protect_content, reply_to_message_id=reply_to_message_id, allow_sending_without_reply=allow_sending_without_reply, reply_markup=reply_markup, **kwargs).send_photo()
        return types.Message_(bot=self.bot, msg=msg)

    def send_video(self, chat_id, video, message_thread_id=None, duration=None, width=None, height=None, thumb=None, caption=None, parse_mode=None, caption_entities=None, supports_streaming=None, disable_notification=False, protect_content=False, reply_to=None, reply_to_message_id=None, allow_sending_without_reply=None, buttons=None, reply_markup=None, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.id
        else:
            _chat_id = chat_id
        if not parse_mode:
            parse_mode = self.default_settings.parse_mode
        if reply_to:
            reply_to_message_id = reply_to
        if buttons:
            reply_markup = buttons
        msg = methods.sendVideo(bot=self.bot, chat_id=_chat_id, video=video, message_thread_id=message_thread_id, duration=duration, width=width, height=height, caption=caption, parse_mode=parse_mode, caption_entities=caption_entities, supports_streaming=supports_streaming, disable_notification=disable_notification, protect_content=protect_content, reply_to_message_id=reply_to_message_id, allow_sending_without_reply=allow_sending_without_reply, reply_markup=reply_markup, **kwargs).send_video()
        return types.Message_(bot=self.bot, msg=msg)

    def send_audio(self, chat_id, audio, message_thread_id=None, caption=None, parse_mode=None, caption_entities=None, duration=None, performer=None, title=None, thumb=None, disable_notification=None, protect_content=False, reply_to=None, reply_to_message_id=None, allow_sending_without_reply=None, buttons=None, reply_markup=None, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.id
        else:
            _chat_id = chat_id
        if not parse_mode:
            parse_mode = self.default_settings.parse_mode
        if reply_to:
            reply_to_message_id = reply_to
        if buttons:
            reply_markup = buttons
        msg = methods.sendAudio(bot=self.bot, chat_id=_chat_id, audio=audio, message_thread_id=message_thread_id, caption=caption, parse_mode=parse_mode, caption_entities=caption_entities, duration=duration, performer=performer, title=title, thumb=thumb, disable_notification=disable_notification, protect_content=protect_content, reply_to_message_id=reply_to_message_id, allow_sending_without_reply=allow_sending_without_reply, reply_markup=reply_markup, **kwargs).send_audio()
        return types.Message_(bot=self.bot, msg=msg)

    def send_document(self, chat_id, document, message_thread_id=None, thumb=None, caption=None, parse_mode=None, caption_entities=None, disable_content_type_detection=None, disable_notification=None, protect_content=False, reply_to=None, reply_to_message_id=None, allow_sending_without_reply=None, buttons=None, reply_markup=None, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.id
        else:
            _chat_id = chat_id
        if not parse_mode:
            parse_mode = self.default_settings.parse_mode
        if reply_to:
            reply_to_message_id = reply_to
        if buttons:
            reply_markup = buttons
        msg = methods.sendDocument(bot=self.bot, chat_id=_chat_id, document=document, message_thread_id=message_thread_id, thumb=thumb, caption=caption, parse_mode=parse_mode, caption_entities=caption_entities, disable_content_type_detection=disable_content_type_detection, disable_notification=disable_notification, protect_content=protect_content, reply_to_message_id=reply_to_message_id, allow_sending_without_reply=allow_sending_without_reply, reply_markup=reply_markup, **kwargs).send_document()
        return types.Message_(bot=self.bot, msg=msg)

    def send_animation(self, chat_id, animation, message_thread_id=None, duration=None, width=None, height=None, thumb=None, caption=None, parse_mode=None, caption_entities=None, disable_notification=None, protect_content=False, reply_to=None, reply_to_message_id=None, allow_sending_without_reply=None, buttons=None, reply_markup=None, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.id
        else:
            _chat_id = chat_id
        if not parse_mode:
            parse_mode = self.default_settings.parse_mode
        if reply_to:
            reply_to_message_id = reply_to
        if buttons:
            reply_markup = buttons
        msg = methods.sendAnimation(bot=self.bot, chat_id=_chat_id, animation=animation, message_thread_id=message_thread_id, duration=duration, width=width, height=height, thumb=thumb, caption=caption, parse_mode=parse_mode, caption_entities=caption_entities, disable_notification=disable_notification, protect_content=protect_content, reply_to_message_id=reply_to_message_id, allow_sending_without_reply=allow_sending_without_reply, reply_markup=reply_markup, **kwargs).send_animation()
        return types.Message_(bot=self.bot, msg=msg)

    def send_voice(self, chat_id, voice, message_thread_id=None, caption=None, parse_mode=None, caption_entities=None, duration=None, disable_notification=None, protect_content=False, reply_to=None, reply_to_message_id=None, allow_sending_without_reply=None, buttons=None, reply_markup=None, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.id
        else:
            _chat_id = chat_id
        if not parse_mode:
            parse_mode = self.default_settings.parse_mode
        if reply_to:
            reply_to_message_id = reply_to
        if buttons:
            reply_markup = buttons
        msg = methods.sendVoice(bot=self.bot, chat_id=_chat_id, voice=voice, message_thread_id=message_thread_id, caption=caption, parse_mode=parse_mode, caption_entities=caption_entities, duration=duration, disable_notification=disable_notification, protect_content=protect_content, reply_to_message_id=reply_to_message_id, allow_sending_without_reply=allow_sending_without_reply, reply_markup=reply_markup, **kwargs).send_voice()
        return types.Message_(bot=self.bot, msg=msg)

    def send_video_note(self, chat_id, video_note, message_thread_id=None, duration=None, length=None, thumb=None, disable_notification=False, protect_content=False, reply_to=None, reply_to_message_id=None, allow_sending_without_reply=None, buttons=None, reply_markup=None, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.id
        else:
            _chat_id = chat_id
        if reply_to:
            reply_to_message_id = reply_to
        if buttons:
            reply_markup = buttons
        msg = methods.sendVideoNote(bot=self.bot, chat_id=_chat_id, video_note=video_note, message_thread_id=message_thread_id, duration=duration, width=width, length=None, caption_entities=caption_entities, disable_notification=disable_notification, protect_content=protect_content, reply_to_message_id=reply_to_message_id, allow_sending_without_reply=allow_sending_without_reply, reply_markup=reply_markup, **kwargs).send_video_note()
        return types.Message_(bot=self.bot, msg=msg)

    def send_media_group(self, chat_id, media, message_thread_id=None, disable_notification=None, protect_content=None, reply_to=None, reply_to_message_id=None, allow_sending_without_reply=None, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.id
        else:
            _chat_id = chat_id
        if reply_to:
            reply_to_message_id = reply_to
        msg = methods.sendMediaGroup(boy=self.bot, chat_id=_chat_id, media=media, message_thread_id=message_thread_id, disable_notification=disable_notification, protect_content=protect_content, reply_to_message_id=reply_to_message_id, allow_sending_without_reply=allow_sending_without_reply, **kwargs).send_media_group()
        return types.Message_(bot=self.bot, msg=msg)

    def send_location(self, chat_id, latitude, longitude, message_thread_id=None, horizontal_accuracy=None, live_period=None, heading=None, proximity_alert_radius=None, disable_notification=None, protect_content=None, reply_to=None, reply_to_message_id=None, allow_sending_without_reply=None, buttons=None, reply_markup=None, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.id
        else:
            _chat_id = chat_id
        if reply_to:
            reply_to_message_id = reply_to
        if buttons:
            reply_markup = buttons
        msg = methods.sendLocation(bot=self.bot, chat_id=_chat_id, latitude=latitude, longitude=longitude, message_thread_id=message_thread_id, horizontal_accuracy=horizontal_accuracy, live_period=live_period, heading=heading, proximity_alert_radius=proximity_alert_radius, disable_notification=disable_notification, protect_content=protect_content, reply_to_message_id=reply_to_message_id, allow_sending_without_reply=allow_sending_without_reply, reply_markup=reply_markup, **kwargs)
        return types.Message_(bot=self.bot, msg=msg)

    def edit_message_live_location(self, latitude, longitude, chat_id=None, message_id=None, inline_message_id=None, heading=None, proximity_alert_radius=None, buttons=None, reply_markup=None, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.id
        else:
            _chat_id = chat_id
        if isinstance(message_id, (types.Message, types.Message_, types.MessageId)):
            _message_id = message_id.message_id
        else:
            _message_id = message_id
        if reply_to:
            reply_to_message_id = reply_to
        if buttons:
            reply_markup = buttons
        msg = methods.editMessageLiveLocation(bot=self.bot, chat_id=_chat_id, message_id=_message_id, inline_message_id=inline_message_id, latitude=latitude, longitude=longitude, horizontal_accuracy=horizontal_accuracy, heading=heading, proximity_alert_radius=proximity_alert_radius, reply_markup=reply_markup, **kwargs)
        return types.Message_(bot=self.bot, msg=msg)

    def send_venue(self, chat_id, latitude, longitude, title, address, message_thread_id=None, foursquare_id=None, foursquare_type=None, google_place_id=None, google_place_type=None, disable_notification=None, protect_content=None, reply_to=None, reply_to_message_id=None, allow_sending_without_reply=None, buttons=None, reply_markup=None, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.id
        else:
            _chat_id = chat_id
        if reply_to:
            reply_to_message_id = reply_to
        if buttons:
            reply_markup = buttons
        msg = methods.sendVenue(bot=self.bot, chat_id=_chat_id, latitude=latitude, longitude=longitude, title=title, address=address, message_thread_id=message_thread_id, foursquare_id=foursquare_id, foursquare_type=foursquare_type, google_place_id=google_place_id, google_place_type=google_place_type, disable_notification=disable_notification, protect_content=protect_content, reply_to_message_id=reply_to_message_id, allow_sending_without_reply=allow_sending_without_reply, reply_markup=reply_markup, **kwargs).send_venue()
        return types.Message_(bot=self.bot, msg=msg)

    def send_contact(self, chat_id, phone_number, first_name, last_name=None, message_thread_id=None, vcard=None, disable_notification=None, protect_content=None, reply_to_message_id=None, allow_sending_without_reply=None, reply_markup=None, **kwargs):
        msg = methods.sendContact(bot=self.bot, chat_id=chat_id, phone_number=phone_number, first_name=first_name, last_name=last_name, message_thread_id=message_thread_id, vcard=vcard, disable_notification=disable_notification, protect_content=protect_content, reply_to_message_id=reply_to_message_id, allow_sending_without_reply=allow_sending_without_reply, reply_markup=reply_markup, **kwargs).send_contact()
        return types.Message_(bot=self.bot, msg=msg)

    def send_poll(self, bot, chat_id, question, options, message_thread_id=None, is_anonymous=None, type=None, allows_multiple_answers=None, correct_option_id=None, explanation=None, explanation_parse_mode=None, explanation_entities=None, open_period=None, close_date=None, is_closed=None, disable_notification=None, protect_content=None, reply_to=None, reply_to_message_id=None, allow_sending_without_reply=None, buttons=None, reply_markup=None, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.id
        else:
            _chat_id = chat_id
        if reply_to:
            reply_to_message_id = reply_to
        if buttons:
            reply_markup = buttons
        msg = methods.sendPoll(bot=self.bot, chat_id=_chat_id, question=question, options=options, message_thread_id=message_thread_id, is_anonymous=is_anonymous, type=type, allows_multiple_answers=allows_multiple_answers, correct_option_id=correct_option_id, explanation=explanation, explanation_parse_mode=explanation_parse_mode, explanation_entities=explanation_entities, open_period=open_period, close_date=close_date, is_closed=is_closed, disable_notification=disable_notification, protect_content=protect_content, reply_to_message_id=reply_to_message_id, allow_sending_without_reply=allow_sending_without_reply, reply_markup=reply_markup, **kwargs).send_poll()
        return types.Message_(bot=self.bot, msg=msg)

    def send_dice(self, chat_id, message_thread_id=None, emoji=None, disable_notification=None, protect_content=None, reply_to=None, reply_to_message_id=None, allow_sending_without_reply=None, buttons=None, reply_markup=None, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.id
        else:
            _chat_id = chat_id
        if reply_to:
            reply_to_message_id = reply_to
        if buttons:
            reply_markup = buttons
        msg = methods.sendDice(bot=self.bot, chat_id=_chat_id, message_thread_id=message_thread_id, emoji=emoji, disable_notification=disable_notification, protect_content=protect_content, reply_to_message_id=reply_to_message_id, allow_sending_without_reply=allow_sending_without_reply, reply_markup=reply_markup, **kwargs)
        return types.Message_(bot=self.bot, msg=msg)

    def send_action(self, chat_id, action, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.id
        else:
            _chat_id = chat_id
        return methods.sendAction(bot=self.bot, chat_id=_chat_id, action=action, **kwargs).send_action()

    def get_user_profile_photos(self, user_id, offset=None, limit=None, **kwargs):
        if isinstance(user_id, types.User):
            _user_id = user_id.chat_id
        elif isinstance(chat_id, types.Message):
            _user_id = user_id.user.id
        else:
            _user_id = user_id
        return methods.getUserProfilePhotos(bot=self.bot, user_id=_user_id, offset=offset, limit=limit, **kwargs).get_user_profile_photos()

    def get_file(self, file_id, **kwargs):
        return methods.getFile(bot=self.bot, file_id=file_id, **kwargs).get_file()

    def ban_user(self, chat_id, user_id, until_date=None, revoke_messages=None, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.id
        elif isinstance(chat_id, types.User):
            _chat_id = chat_id.user_id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.id
        else:
            _chat_id = chat_id
        if isinstance(user_id, types.User):
            _user_id = user_id.id
        elif isinstance(user_id, types.Message):
            _user_id = user_id.user.id
        else:
            _user_id = user_id
        return methods.banChatMember(bot=self.bot, chat_id=_chat_id, user_id=_user_id, until_date=until_date, revoke_messages=revoke_messages, **kwargs).ban_chat_member()

    def unban_user(self, chat_id, user_id, only_if_banned=True, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.id
        else:
            _chat_id = chat_id
        if isinstance(user_id, types.User):
            _user_id = user_id.id
        elif isinstance(user_id, types.Message):
            _user_id = user_id.user.id
        else:
            _user_id = user_id
        return methods.unbanChatMember(bot=self.bot, chat_id=_chat_id, user_id=_user_id, only_if_banned=only_if_banned, **kwargs).unban_chat_member()

    def restrict_user(self, chat_id, user_id, permissions, until_date, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.id
        else:
            _chat_id = chat_id
        if isinstance(user_id, types.User):
            _user_id = user_id.id
        elif isinstance(user_id, types.Message):
            _user_id = user_id.user.id
        else:
            _user_id = user_id
        return methods.restrictChatMember(bot=self.bot, chat_id=_chat_id, permissions=permissions, until_date=until_date, **kwargs).restrict_chat_member()

    def promote_user(self, chat_id, user_id, is_anonymous=None, can_manage_topics=None, can_manage_chat=None, can_post_messages=None, can_edit_messages=None, can_delete_messages=None, can_manage_video_chats=None, can_restrict_members=None, can_promote_members=None, can_change_info=None, can_invite_users=None, can_pin_messages=None, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.id
        else:
            _chat_id = chat_id
        if isinstance(user_id, types.User):
            _user_id = user_id.id
        elif isinstance(user_id, types.Message):
            _user_id = user_id.user.id
        else:
            _user_id = user_id
        return methods.promoteChatMember(bot=self.bot, chat_id=_chat_id, user_id=_user_id, is_anonymous=is_anonymous, can_manage_topics=can_manage_topics, can_manage_chat=can_manage_chat, can_post_messages=can_post_messages, can_edit_messages=can_edit_messages, can_delete_messages=can_delete_messages, can_manage_video_chats=can_manage_video_chats, can_restrict_members=can_restrict_members, can_promote_members=can_promote_members, can_change_info=can_change_info, can_invite_users=can_invite_users, can_pin_messages=can_pin_messages, **kwargs).promote_chat_member()

    def set_chat_administrator_custom_title(self, chat_id, user_id, custom_title, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.id
        else:
            _chat_id = chat_id
        if isinstance(user_id, types.User):
            _user_id = user_id.id
        elif isinstance(user_id, types.Message):
            _user_id = user_id.user.id
        else:
            _user_id = user_id
        return methods.setChatAdministratorCustomTitle(bot=self.bot, chat_id=_chat_id, user_id=_user_id, custom_title=custom_title, **kwargs).set_chat_administrator_custom_title()

    def ban_chat(self, chat_id, sender_chat_id, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.id
        else:
            _chat_id = chat_id
        if isinstance(sender_chat_id, types.Chat):
            _sender_id = sender_chat_id.id
        elif isinstance(sender_chat_id, types.Message):
            _sender_id = sender_chat_id.chat.id
        else:
            _sender_id = sender_chat_id
        return methods.banChatSenderChat(bot=self.bot, chat_id=_chat_id, sender_chat_id=_sender_chat_id, **kwargs).ban_chat_sender_chat()

    def unban_chat(self, chat_id, sender_chat_id, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.id
        else:
            _chat_id = chat_id
        if isinstance(sender_chat_id, types.Chat):
            _sender_id = sender_chat_id.id
        elif isinstance(sender_chat_id, types.Message):
            _sender_id = sender_chat_id.chat.id
        else:
            _sender_id = sender_chat_id
        return methods.unbanChatSenderChat(bot=self.bot, chat_id=_chat_id, sender_chat_id=_sender_chat_id, **kwargs).unban_chat_sender_chat()

    def set_chat_permissions(self, chat_id, permissions, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.id
        else:
            _chat_id = chat_id
        return methods.setChatPermissions(bot=self.bot, chat_id=_chat_id, permissions=permissions, **kwargs).set_chat_permissions()

    def export_chat_invite_link(self, chat_id, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.id
        else:
            _chat_id = chat_id
        return methods.exportChatInviteLink(bot=self.bot, chat_id=_chat_id, **kwargs).export_chat_invite_link()

    def create_chat_invite_link(self, chat_id, name=None, expire_date=None, member_limit=None, creates_join_request=None, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.id
        else:
            _chat_id = chat_id
        return methods.createChatInviteLink(bot=self.bot, chat_id=_chat_id, name=name, expire_date=expire_date, member_limit=member_limit, creates_join_request=creates_join_request, **kwargs).create_chat_invite_link()

    def edit_chat_invite_link(self, chat_id, invite_link, name=None, expire_date=None, member_limit=None, creates_join_request=None, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.id
        else:
            _chat_id = chat_id
        return methods.editChatInviteLink(bot=self.bot, chat_id=_chat_id, invite_link=invite_link, name=name, expire_date=expire_date, member_limit=member_limit, creates_join_request=creates_join_request, **kwargs).editChatInviteLink()

    def revoke_chat_invite_link(self, chat_id, invite_link, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.id
        else:
            _chat_id = chat_id
        return methods.revokeChatInviteLink(bot=self.bot, chat_id=_chat_id, invite_link=invite_link, **kwargs).revoke_chat_invite_link()

    def approve_chat_join_request(self, chat_id, user_id, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.id
        else:
            _chat_id = chat_id
        if isinstance(user_id, types.User):
            _user_id = user_id.id
        elif isinstance(user_id, types.Message):
            _user_id = user_id.user.chat_id
        else:
            _user_id = user_id
        return methods.approveChatJoinRequest(bot=self.bot, chat_id=_chat_id, user_id=_user_id, **kwargs).approve_chat_join_request()

    def decline_chat_join_request(self, chat_id, user_id, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.id
        else:
            _chat_id = chat_id
        if isinstance(user_id, types.User):
            _user_id = user_id.id
        elif isinstance(user_id, types.Message):
            _user_id = user_id.user.chat_id
        else:
            _user_id = user_id
        return methods.declineChatJoinRequest(bot=self.bot, chat_id=_chat_id, user_id=_user_id, **kwargs).decline_chat_join_request()

    def set_chat_photo(self, chat_id, photo, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.id
        else:
            _chat_id = chat_id
        return methods.setChatPhoto(bot=self.bot, chat_id=_chat_id, photo=photo, **kwargs).set_chat_photo()

    def delete_chat_photo(self, chat_id, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.id
        else:
            _chat_id = chat_id
        return methods.deleteChatPhoto(bot=self.bot, chat_id=_chat_id, **kwargs).delete_chat_photo()

    def set_chat_title(self, chat_id, title, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.id
        else:
            _chat_id = chat_id
        return methods.setChatTitle(bot=self.bot, chat_id=_chat_id, title=title, **kwargs).set_chat_title()

    def set_chat_description(self, chat_id, description, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.id
        else:
            _chat_id = chat_id
        return methods.setChatDescription(bot=self.bot, description=description).set_chat_description()

    def pin_chat_message(self, chat_id, message_id, disable_notification=None, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.id
        else:
            _chat_id = chat_id
        if isinstance(message_id, (types.Message, types.Message_, types.MessageId)):
            _message_id = message_id.message_id
        else:
            _message_id = message_id
        return methods.pinChatMessage(bot=self.bot, message_id=_message_id, disable_notification=disable_notification, **kwargs).pin_chat_message()

    # Short-Hand-Method for pin_chat_message.
    def pin_message(self, chat_id, message_id, disable_notification=None, **kwargs):
        return self.pin_chat_message(chat_id=chat_id, message_id=message_id, disable_notification=disable_notification, **kwargs)

    def unpin_chat_message(self, chat_id, message_id, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.id
        else:
            _chat_id = chat_id
        if isinstance(message_id, (types.Message, types.Message_, types.MessageId)):
            _message_id = message_id.message_id
        else:
            _message_id = message_id
        return methods.unpinChatMessage(bot=self.bot, message_id=_message_id, **kwargs).unpin_chat_message()

    # Short-Hand-Method for unpin_chat_message.
    def unpin_message(self, chat_id, message_id, disable_notification=None, **kwargs):
        return self.unpin_chat_message(chat_id=chat_id, message_id=message_id, disable_notification=disable_notification, **kwargs)

    def unpin_all_chat_messages(self, chat_id, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.id
        else:
            _chat_id = chat_id
        return methods.unpinAllChatMessages(bot=self.bot, chat_id=_chat_id, **kwargs).unpin_all_chat_messages()

    # Short-Hand-Method for unpin_all_chat_messages.
    def unpin_all_messages(self, chat_id):
        return self.unpin_all_chat_messages(chat_id=chat_id)

    def leave_chat(self, chat_id, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.id
        else:
            _chat_id = chat_id
        return methods.leaveChat(bot=self.bot, chat_id=_chat_id, **kwargs).leave_chat()

    def get_chat(self, chat_id, *args, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.id
        elif isinstance(chat_id, types.User):
            _chat_id = chat_id.user_id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.id
        else:
            _chat_id = chat_id
        return methods.getChat(bot=self.bot, chat_id=_chat_id, **kwargs).get_chat()

    def get_chat_administrators(self, chat_id, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.id
        elif isinstance(chat_id, types.User):
            _chat_id = chat_id.user_id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.id
        else:
            _chat_id = chat_id
        return methods.getChatAdministrators(bot=self.bot, chat_id=_chat_id, **kwargs).get_chat_administrators()

    # Short-Hand-Method for get_chat_administrators.
    def getAdmins(self, chat_id, **kwargs):
        return self.get_chat_administrators(chat_id=chat_id, **kwargs)

    def get_chat_member_count(self, chat_id):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.id
        else:
            _chat_id = chat_id
        return methods.getChatMemberCount(bot=self.bot, chat_id=_chat_id, **kwargs).get_chat_member_count()

    def get_chat_member(self, chat_id, user_id, *args, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.id
        else:
            _chat_id = chat_id
        if isinstance(user_id, types.User):
            _user_id = user_id.id
        elif isinstance(user_id, types.Message):
            _user_id = user_id.user.id
        else:
            _user_id = user_id
        return methods.getChatMember(bot=self.bot, chat_id=_chat_id, user_id=_user_id, **kwargs).get_chat_member()

    def set_chat_sticker_set(self, chat_id, sticker_set_name, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.id
        else:
            _chat_id = chat_id
        return methods.setChatStickerSet(bot=self.bot, sticker_set_name=sticker_set_name, **kwargs).set_chat_sticker_set()

    def delete_chat_sticker_set(self, chat_id, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.id
        else:
            _chat_id = chat_id
        return methods.deleteChatStickerSet(bot=self.bot, **kwargs).delete_chat_sticker_set()

    def get_forum_topic_icon_stickers(self, **kwargs):
        return methods.getForumTopicIconStickers(bot=self.bot, **kwargs).get_forum_topic_icon_stickers()

    def create_forum_topic(self, chat_id, name, icon_color=None, icon_custom_emoji_id=None, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.id
        else:
            _chat_id = chat_id
        return methods.createForumTopic(bot=self.bot, chat_id=_chat_id, name=name, icon_color=icon_color, icon_custom_emoji_id=icon_custom_emoji_id, **kwargs).create_forum_topic()

    def edit_forum_topic(self, chat_id, name, icon_color, icon_custom_emoji_id, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.id
        else:
            _chat_id = chat_id
        return methods.editForumTopic(bot=self.bot, chat_id=_chat_id, name=name, icon_color=icon_color, icon_custom_emoji_id=icon_custom_emoji_id, **kwargs).edit_forum_topic()

    def close_forum_topic(self, chat_id, message_thread_id, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.id
        else:
            _chat_id = chat_id
        return methods.closeForumTopic(bot=self.bot, chat_id=_chat_id, message_thread_id=message_thread_id, **kwargs).close_forum_topic()

    def reopen_forum_topic(self, chat_id, message_thread_id, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.id
        else:
            _chat_id = chat_id
        return methods.reopenForumTopic(bot=self.bot, chat_id=_chat_id, message_thread_id=message_thread_id, **kwargs).reopen_forum_topic()

    def delete_forum_topic(self, chat_id, message_thread_id, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.id
        else:
            _chat_id = chat_id
        return methods.deleteForumTopic(bot=self.bot, chat_id=_chat_id, message_thread_id=message_thread_id, **kwargs).delete_forum_topic()

    def unpin_all_forum_topic_messages(self, chat_id, message_thread_id, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.id
        else:
            _chat_id = chat_id
        return methods.unpinAllForumTopicMessages(bot=self.bot, chat_id=_chat_id, message_thread_id=message_thread_id, **kwargs).unpin_all_forum_topic_messages()

    def answer_callback_query(self, callback_query_id, text=None, show_alert=False, url=None, cache_time=0, **kwargs):
        return methods.answerCallbackQuery(bot=self.bot, callback_query_id=callback_query_id, text=text, show_alert=show_alert, url=url, cache_time=cache_time, **kwargs).answer_callback_query()

    def set_my_commands(self, commands, scope=None, language_code=None, **kwargs):
        return methods.setMyCommands(bot=self.bot, commands=commands, scope=scope, language_code=language_code, **kwargs).set_my_commands()

    def delete_my_commands(self, scope=None, language_code=None, **kwargs):
        return methods.deleteMyCommands(bot=self.bot, scope=scope, language_code=language_code, **kwargs).delete_my_commands()

    def get_my_commands(self, scope=None, language_code=None, **kwargs):
        return methods.getMyCommands(bot=self.bot, scope=scope, language_code=language_code, **kwargs).get_my_commands()

    def set_chat_menu_button(self, chat_id=None, menu_button=None, **kwargs):
        return methods.setChatMenuButton(bot=self.bot, chat_id=chat_id, menu_button=menu_button).set_chat_menu_button()

    def get_chat_menu_button(self, chat_id=None, **kwargs):
        return methods.setChatMenuButton(bot=self.bot, chat_id=chat_id).get_chat_menu_button()

    def set_my_default_administrator_rights(self, rights=None, for_channels=None, **kwargs):
        return methods.setMyDefaultAdministratorRights(bot=self.bot, rights=rights, for_channels=for_channels, **kwargs).set_my_default_administrator_rights()

    def get_my_default_administrator_rights(self, for_channels=None, **kwargs):
        return methods.setMyDefaultAdministratorRights(bot=self.bot, for_channels=for_channels, **kwargs).get_my_default_administrator_rights()

    def edit_message_text(self, text, chat_id=None, message_id=None, inline_message_id=None, parse_mode=None, entities=None, link_preview=None, disable_web_page_preview=None, buttons=None, reply_markup=None, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.id
        elif isinstance(chat_id, types.User):
            _chat_id = chat_id.user_id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.id
        else:
            _chat_id = chat_id
        if isinstance(message_id, (types.Message, types.Message_, types.MessageId)):
            _message_id = message_id.message_id
        else:
            _message_id = message_id
        if not parse_mode:
            parse_mode = self.default_settings.parse_mode
        if link_preview:
            disable_web_page_preview = link_preview
        elif disable_web_page_preview:
            pass
        else:
            disable_web_page_preview = self.default_settings.link_preview 
        if buttons:
            reply_markup = buttons
        msg = methods.editMessageText(bot=self.bot, chat_id=_chat_id, message_id=_message_id, inline_message_id=inline_message_id, text=text, parse_mode=parse_mode, entities=entities, disable_web_page_preview=disable_web_page_preview, reply_markup=reply_markup, **kwargs).edit_message_text()
        if msg is True:
            return msg
        else:
            return types.Message_(bot=self.bot, msg=msg)

    def edit_message_caption(self, chat_id=None, message_id=None, inline_message_id=None, caption=None, parse_mode=None, caption_entities=None, buttons=None, reply_markup=None, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.id
        elif isinstance(chat_id, types.User):
            _chat_id = chat_id.user_id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.id
        else:
            _chat_id = chat_id
        if isinstance(message_id, (types.Message, types.Message_, types.MessageId)):
            _message_id = message_id.message_id
        else:
            _message_id = message_id
        if not parse_mode:
            parse_mode = self.default_settings.parse_mode
        if buttons:
            reply_markup = buttons
        msg = methods.editMessageCaption(bot=self.bot, chat_id=_chat_id, message_id=_message_id, inline_message_id=inline_message_id, caption=caption, parse_mode=parse_mode, caption_entities=caption_entities, reply_markup=reply_markup, **kwargs).edit_message_caption()
        if msg is True:
            return msg
        else:
            return types.Message_(bot=self.bot, msg=msg)

    def edit_message_media(self, media, chat_id=None, message_id=None, inline_message_id=None, buttons=None, reply_markup=None, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.id
        elif isinstance(chat_id, types.User):
            _chat_id = chat_id.user_id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.id
        else:
            _chat_id = chat_id
        if isinstance(message_id, (types.Message, types.Message_, types.MessageId)):
            _message_id = message_id.message_id
        else:
            _message_id = message_id
        if not parse_mode:
            parse_mode = self.default_settings.parse_mode
        if buttons:
            reply_markup = buttons
        msg = methods.editMessageMedia(bot=self.bot, chat_id=_chat_id, message_id=_message_id, inline_message_id=inline_message_id, media=media, reply_markup=reply_markup, **kwargs).edit_message_media()
        if msg is True:
            return msg
        else:
            return types.Message_(bot=self.bot, msg=msg)

    def edit_message_reply_markup(self, chat_id=None, message_id=None, inline_message_id=None, buttons=None, reply_markup=None, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.id
        elif isinstance(chat_id, types.User):
            _chat_id = chat_id.user_id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.id
        else:
            _chat_id = chat_id
        if isinstance(message_id, (types.Message, types.Message_, types.MessageId)):
            _message_id = message_id.message_id
        else:
            _message_id = message_id
        if not parse_mode:
            parse_mode = self.default_settings.parse_mode
        if buttons:
            reply_markup = buttons
        msg = methods.editMessageReplyMarkup(bot=self.bot, chat_id=_chat_id, message_id=_message_id, inline_message_id=inline_message_id, reply_markup=reply_markup, **kwargs).edit_message_reply_markup()
        if msg is True:
            return msg
        else:
            return types.Message_(bot=self.bot, msg=msg)

    def stop_poll(self, chat_id, message_id, buttons=None, reply_markup=None, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.id
        elif isinstance(chat_id, types.User):
            _chat_id = chat_id.user_id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.id
        else:
            _chat_id = chat_id
        if isinstance(message_id, (types.Message, types.Message_, types.MessageId)):
            _message_id = message_id.message_id
        else:
            _message_id = message_id
        if buttons:
            reply_markup = buttons
        return methods.stopPoll(bot=self.bot, chat_id=_chat_id, message_id=_message_id, reply_markup=reply_markup, **kwargs)

    def send_sticker(self, chat_id, sticker, disable_notification=None, protect_content=None, reply_to=None, reply_to_message_id=None, allow_sending_without_reply=None, buttons=None, reply_markup=None, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.id
        elif isinstance(chat_id, types.User):
            _chat_id = chat_id.user_id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.id
        else:
            _chat_id = chat_id
        if isinstance(message_id, (types.Message, types.Message_, types.MessageId)):
            _message_id = message_id.message_id
        else:
            _message_id = message_id
        if reply_to:
            reply_markup = reply_to
        if buttons:
            reply_markup = buttons
        msg = methods.sendSticker(bot=self.bot, chat_id=chat_id, sticker=sticker, disable_notification=disable_notification, protect_content=protect_content, reply_to_message_id=reply_to_message_id, allow_sending_without_reply=allow_sending_without_reply, reply_markup=reply_markup, **kwargs).send_sticker()
        return types.Message_(bot=self.bot, msg=msg)

    def get_sticker_set(self, name, **kwargs):
        return methods.getStickerSet(bot=self.bot, name=name, **kwargs)

    def get_custom_emoji_sticker(self, custom_emoji_ids, **kwargs):
        return methods.getCustomEmojiStickers(bot=self.bot, custom_emoji_ids=custom_emoji_ids, **kwargs)

    def upload_sticker_file(self, user_id, png_sticker, **kwargs):
        if isinstance(user_id, types.User):
            _user_id = user_id.id
        elif isinstance(user_id, types.Message):
            _user_id = user_id.user.id
        else:
            _user_id = user_id
        return methods.uploadStickerFile(bot=self.bot, user_id=_user_id, png_sticker=png_sticker, **kwargs)

    # Short-Hand-Method for upload_sticker_file.
    def upload_sticker(self, user_id, png_sticker, **kwargs):
        return self.upload_sticker_file(user_id=user_id, png_sticker=png_sticker, **kwargs)

    def create_new_sticker_set(self, user_id, name, title, emojis, png_sticker=None, tgs_sticker=None, webm_sticker=None, sticker_type=None, mask_position=None, **kwargs):
        if isinstance(user_id, types.User):
            _user_id = user_id.id
        elif isinstance(user_id, types.Message):
            _user_id = user_id.user.id
        else:
            _user_id = user_id
        return methods.createNewStickerSet(bot=self.bot, user_id=user_id, name=name, title=title, emojis=emojis, png_sticker=png_sticker, tgs_sticker=tgs_sticker, webm_sticker=webm_sticker, sticker_type=sticker_type, mask_position=mask_position, **kwargs).create_new_sticker_set()

    def add_sticker_to_set(self, user_id, name, emojis, png_sticker=None, tgs_sticker=None, webm_sticker=None, mask_position=None, **kwargs):
        if isinstance(user_id, types.User):
            _user_id = user_id.id
        elif isinstance(user_id, types.Message):
            _user_id = user_id.user.id
        else:
            _user_id = user_id
        return methods.addStickerToSet(bot=self.bot, user_id=user_id, name=name, emojis=emojis, png_sticker=png_sticker, tgs_sticker=tgs_sticker, webm_sticker=webm_sticker, mask_position=mask_position, **kwargs).add_sticker_to_set()

    def set_sticker_position_in_set(self, sticker, position, **kwargs):
        return methods.setStickerPositionInSet(bot=self.bot, sticker=sticker, position=position, **kwargs).set_sticker_position_in_set()

    def delete_sticker_from_set(self, sticker, **kwargs):
        return methods.deleteStickerFromSet(bot=self.bot, sticker=sticker, **kwargs).delete_sticker_from_set()

    def set_sticker_set_thumb(self, name, user_id, thumb=None, **kwargs):
        if isinstance(user_id, types.User):
            _user_id = user_id.id
        elif isinstance(user_id, types.Message):
            _user_id = user_id.user.id
        else:
            _user_id = user_id
        return methods.setStickerSetThumb(bot=self.bot, user_id=_user_id, thumb=thumb, **kwargs).set_sticker_set_thumb()

    # Own created methods.
    def get_permissions(self, chat_id, user_id=None, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.id
        else:
            _chat_id = chat_id
        if isinstance(user_id, types.User):
            _user_id = user_id.id
        elif isinstance(user_id, types.Message):
            _user_id = user_id.user.id
        else:
            _user_id = user_id
        return methods.getPermissions(bot=self.bot, chat_id=_chat_id, user_id=_user_id, **kwargs).get_permissions()