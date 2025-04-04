import sys
import os
import tkinter as tk
from tkinter import filedialog

def create_replay_html(log_content, output_path):
    print("Creating replay HTML file...")
    # HTML template with escaped curly braces and placeholder for battle log
    html_template = '''<!DOCTYPE html>
<meta charset="utf-8" />
<!-- version 1 -->
<title>[Gen 9] Random Battle replay: BOT1 vs. BOT2</title>
<style>
html,body {{font-family:Verdana, sans-serif;font-size:10pt;margin:0;padding:0;}}body{{padding:12px 0;}} .battle-log {{font-family:Verdana, sans-serif;font-size:10pt;}} .battle-log-inline {{border:1px solid #AAAAAA;background:#EEF2F5;color:black;max-width:640px;margin:0 auto 80px;padding-bottom:5px;}} .battle-log .inner {{padding:4px 8px 0px 8px;}} .battle-log .inner-preempt {{padding:0 8px 4px 8px;}} .battle-log .inner-after {{margin-top:0.5em;}} .battle-log h2 {{margin:0.5em -8px;padding:4px 8px;border:1px solid #AAAAAA;background:#E0E7EA;border-left:0;border-right:0;font-family:Verdana, sans-serif;font-size:13pt;}} .battle-log .chat {{vertical-align:middle;padding:3px 0 3px 0;font-size:8pt;}} .battle-log .chat strong {{color:#40576A;}} .battle-log .chat em {{padding:1px 4px 1px 3px;color:#000000;font-style:normal;}} .chat.mine {{background:rgba(0,0,0,0.05);margin-left:-8px;margin-right:-8px;padding-left:8px;padding-right:8px;}} .spoiler {{color:#BBBBBB;background:#BBBBBB;padding:0px 3px;}} .spoiler:hover, .spoiler:active, .spoiler-shown {{color:#000000;background:#E2E2E2;padding:0px 3px;}} .spoiler a {{color:#BBBBBB;}} .spoiler:hover a, .spoiler:active a, .spoiler-shown a {{color:#2288CC;}} .chat code, .chat .spoiler:hover code, .chat .spoiler:active code, .chat .spoiler-shown code {{border:1px solid #C0C0C0;background:#EEEEEE;color:black;padding:0 2px;}} .chat .spoiler code {{border:1px solid #CCCCCC;background:#CCCCCC;color:#CCCCCC;}} .battle-log .rated {{padding:3px 4px;}} .battle-log .rated strong {{color:white;background:#89A;padding:1px 4px;border-radius:4px;}} .spacer {{margin-top:0.5em;}} .message-announce {{background:#6688AA;color:white;padding:1px 4px 2px;}} .message-announce a, .broadcast-green a, .broadcast-blue a, .broadcast-red a {{color:#DDEEFF;}} .broadcast-green {{background-color:#559955;color:white;padding:2px 4px;}} .broadcast-blue {{background-color:#6688AA;color:white;padding:2px 4px;}} .infobox {{border:1px solid #6688AA;padding:2px 4px;}} .infobox-limited {{max-height:200px;overflow:auto;overflow-x:hidden;}} .broadcast-red {{background-color:#AA5544;color:white;padding:2px 4px;}} .message-learn-canlearn {{font-weight:bold;color:#228822;text-decoration:underline;}} .message-learn-cannotlearn {{font-weight:bold;color:#CC2222;text-decoration:underline;}} .message-effect-weak {{font-weight:bold;color:#CC2222;}} .message-effect-resist {{font-weight:bold;color:#6688AA;}} .message-effect-immune {{font-weight:bold;color:#666666;}} .message-learn-list {{margin-top:0;margin-bottom:0;}} .message-throttle-notice, .message-error {{color:#992222;}} .message-overflow, .chat small.message-overflow {{font-size:0pt;}} .message-overflow::before {{font-size:9pt;content:'...';}} .subtle {{color:#3A4A66;}}
</style>
<div class="wrapper replay-wrapper" style="max-width:1180px;margin:0 auto">
<input type="hidden" name="replayid" value="unregisteredserver-gen9randombattle-1" />
<div class="battle"></div><div class="battle-log"></div><div class="replay-controls"></div><div class="replay-controls-2"></div>
<h1 style="font-weight:normal;text-align:center"><strong>[Gen 9] Random Battle</strong><br /><a">BOT1</a> vs. <a" class="subtle" target="_blank">BOT2</a></h1>
<script type="text/plain" class="battle-log-data">{battle_log}</script>
</div>
<script>
let daily = Math.floor(Date.now()/1000/60/60/24);document.write('<script src="https://play.pokemonshowdown.com/js/replay-embed.js?version'+daily+'"></'+'script>');
</script>
<script>(function(){{function c(){{var b=a.contentDocument||a.contentWindow.document;if(b){{var d=b.createElement('script');d.innerHTML="window.__CF$cv$params={{r:'928b36e9ddecb038',t:'MTc0MzM3NTUzNS4wMDAwMDA='}};var a=document.createElement('script');a.nonce='';a.src='/cdn-cgi/challenge-platform/scripts/jsd/main.js';document.getElementsByTagName('head')[0].appendChild(a);";b.getElementsByTagName('head')[0].appendChild(d)}}}}if(document.body){{var a=document.createElement('iframe');a.height=1;a.width=1;a.style.position='absolute';a.style.top=0;a.style.left=0;a.style.border='none';a.style.visibility='hidden';document.body.appendChild(a);if('loading'!==document.readyState)c();else if(window.addEventListener)document.addEventListener('DOMContentLoaded',c);else{{var e=document.onreadystatechange||function(){{}};document.onreadystatechange=function(b){{e(b);'loading'!==document.readyState&&(document.onreadystatechange=e,c())}}}}}}}})();</script>
'''

    try:
        # Replace the placeholder with the battle log content
        html_content = html_template.format(battle_log=log_content)
        # Write to output file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        print(f"Replay HTML file created at: {output_path}")
    except Exception as e:
        print(f"Error creating HTML file: {e}")
        sys.exit(1)

def main():
    print("Starting script...")
    
    # Check if a file path was provided as a command-line argument
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        print(f"Using file path from command line: {file_path}")
        if not os.path.exists(file_path):
            print(f"Error: File '{file_path}' does not exist.")
            sys.exit(1)
    else:
        # Fallback to Tkinter file dialog if no argument provided
        print("No file path provided. Opening file dialog...")
        try:
            root = tk.Tk()
            root.withdraw()  # Hide the root window
            file_path = filedialog.askopenfilename(
                title="Select Battle Log File",
                filetypes=(("Text files", "*.txt"), ("All files", "*.*"))
            )
            root.destroy()
            if not file_path:
                print("No file selected. Exiting...")
                sys.exit(0)
        except Exception as e:
            print(f"Error with file dialog: {e}")
            print("Please run the script with a file path argument (e.g., 'python replay_test.py mylog.txt')")
            sys.exit(1)

    # Read the battle log content
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            battle_log_content = f.read()
        print("Battle log file read successfully.")
    except Exception as e:
        print(f"Error reading file '{file_path}': {e}")
        sys.exit(1)

    # Generate output filename
    output_dir = os.path.dirname(file_path)
    output_filename = os.path.splitext(os.path.basename(file_path))[0] + "_replay.html"
    output_path = os.path.join(output_dir, output_filename)

    # Create the replay HTML file
    create_replay_html(battle_log_content, output_path)

if __name__ == "__main__":
    main()