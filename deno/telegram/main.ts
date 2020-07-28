// @ts-ignore
const url = ["https://api.telegram.org/bot", Deno.env.get('BOT_KEY'), "/"].join('');
import {v4} from "https://deno.land/std/uuid/mod.ts";

var offset = 0;
var tries = 0;

/**
 *
 */
function getPhotoReply(user_id: number) {
  return {
    type: 'photo',
    id: v4.generate(),
    photo_url: 'https://homepages.cae.wisc.edu/~ece533/images/airplane.png',
    thumb_url: 'https://via.placeholder.com/150'
  }
}

/**
 *
 */
function getGifReply(user_id: number) {
  return {
    type: 'gif',
    id: v4.generate(),
    gif_url: 'https://media.giphy.com/media/3orieNX1KVm2F03Dxu/giphy.gif',
    thumb_url: 'https://media.giphy.com/media/3orieNX1KVm2F03Dxu/giphy.gif'
  }
}

/**
 *
 * @param query_id
 */
async function sendInlineQueries(query_id: number) {
  console.log("sending inline query", query_id);
  let body = JSON.stringify({
    results: [getGifReply(query_id), getPhotoReply(query_id)],
    inline_query_id: String(query_id)
  });
  console.log(body);
  let r = await fetch(url + 'answerInlineQuery', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: body
  })
  console.log(r);
}

async function sendMessage(to: any[]) {
  console.log(to);
  for (let user of to) {
    await fetch(url + 'sendMessage', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        chat_id: user['id'],
        text: 'hello <b>' + user['first_name'] + '</b>',
        parse_mode: 'HTML'
      })
    })
  }

}

/**
 *
 */
async function getUpdates() {
  console.log(url + 'getMe');
  let r = await fetch(url + 'getUpdates?offest=' + offset);
  let body = await r.json();
  let ids = [];
  let content = body.result;
  offset = content.update_id++;
  console.log(body);
  for (let entry of content) {
    offset = Math.max(entry.update_id, offset);
    if (entry.inline_query) {
      await sendInlineQueries(entry.inline_query.id);
    } else {
      ids.push(entry.message.from);
    }
  }
  if (tries++ < 20) {
    setTimeout(getUpdates, 2000)
  }
}


await getUpdates();

// inline_query_id
// results
// => type
// => photo_url
// => type
