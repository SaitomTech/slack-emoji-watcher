# slack-emoji-watcher

## 使用方法

- 環境変数の設定
  - `.env` ファイルをディレクトリ直下に作成

  ```text
  SLACK_BOT_TOKEN=使用するbotのtoken（Bot User OAuth Token）
  SLACK_APP_TOKEN=使用するappのtoken（API level Token）
  CHANNEL_ID=投稿するチャンネルID（チャンネル名ではない。ブラウザのURLから確認）
  ```

- vscodeで `open folder in container`
- `$ python bot.py` を実行

## 参考

- slack_boltについて

  - https://slack.dev/bolt-python/tutorial/getting-started
