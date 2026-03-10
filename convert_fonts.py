import os
import subprocess
import time

from rich import print
from libs.buffer import addToClipBoardFile

start_time = time.time()


def convertFontsFunc():
    def checkInstalledApps():
        retval = subprocess.call(["which", "woff2_compress"])
        if retval != 0:
            print("Packagename not installed!")
            subprocess.call(["sudo", "apt", "install", "woff2", "-y"])

        retval = os.system("npm ls -g | grep ttf2woff")
        if retval != 0:
            print("Packagename not installed!")
            os.system("npm install -g ttf2woff")

    checkInstalledApps()

    def validateFontFiles():
        ttf_files = [f for f in os.listdir(".") if f.endswith(".ttf")]
        woff_files = [f for f in os.listdir(".") if f.endswith(".woff")]
        woff2_files = [f for f in os.listdir(".") if f.endswith(".woff2")]
        if not ttf_files and not woff_files and not woff2_files:
            print(
                "\n[bold red][ERROR][/bold red] No [yellow].ttf[/yellow], [yellow].woff[/yellow] or [yellow].woff2[/yellow] files found in the current directory."
            )
            print(
                "[dim]Expected format:[/dim] [bold]FontName-Weight.ttf[/bold] [dim]or[/dim] [bold]FontName-Weight.woff[/bold]"
            )
            print("\n[bold]Examples:[/bold]")
            print("  [green]Roboto-Regular.ttf[/green]")
            print("  [green]Roboto-Bold.ttf[/green]")
            print("  [green]Roboto-Italic.ttf[/green]")
            print("  [green]Roboto-Light.ttf[/green]")
            print("  [green]Roboto-ExtraBold.ttf[/green]")
            print("  [green]Roboto-SemiBold.ttf[/green]")
            print(
                "\n[dim]Run the script from the folder containing your font files.[/dim]"
            )
            return False
        return True

    if not validateFontFiles():
        return

    def ttfToWoff2():
        ttf_files = [f for f in os.listdir(".") if f.endswith(".ttf")]
        if not ttf_files:
            return
        for file in ttf_files:
            subprocess.call(["ttf2woff", file, file.replace(".ttf", ".woff")])
            subprocess.call(["woff2_compress", file])
            os.remove(file)

    ttfToWoff2()

    def woffToCss():
        woff_files = [f for f in os.listdir(".") if f.endswith(".woff")]
        woff2_files = [f for f in os.listdir(".") if f.endswith(".woff2")]
        # use woff as base; fall back to woff2 if no woff files
        if woff_files:
            base_files = woff_files
            base_ext = ".woff"
        else:
            base_files = woff2_files
            base_ext = ".woff2"
        # create file fonts.css
        f = open("fonts.css", "w")
        rel_path = input(
            "Enter relative path to fonts folder (default: assets/fonts): "
        )
        if rel_path == "":
            rel_path = "assets/fonts"
        for file in base_files:
            file_name_without_extension = file.replace(base_ext, "")
            file_name_without_extension_lower = file_name_without_extension.lower()
            font_style = "normal"
            font_weight = "normal"
            print(file_name_without_extension_lower)

            if "italic" in file_name_without_extension_lower:
                font_style = "italic"

            if "extralight" in file_name_without_extension_lower:
                font_weight = "200"
            elif "light" in file_name_without_extension_lower:
                font_weight = "300"
            if "extrabold" in file_name_without_extension_lower:
                font_weight = "800"
            elif "bold" in file_name_without_extension_lower:
                font_weight = "700"
            if "thin" in file_name_without_extension_lower:
                font_weight = "100"
            if "medium" in file_name_without_extension_lower:
                font_weight = "500"
            if (
                "semibold" in file_name_without_extension_lower
                or "demibold" in file_name_without_extension_lower
            ):
                font_weight = "600"
            if (
                "black" in file_name_without_extension_lower
                or "heavy" in file_name_without_extension_lower
            ):
                font_weight = "900"

            font_name = file_name_without_extension
            capital_name = font_name.capitalize()
            capital_name = capital_name.split("-")[0]
            has_woff2 = os.path.exists(f"{font_name}.woff2")
            has_woff = os.path.exists(f"{font_name}.woff")
            src_parts = []
            if has_woff2:
                src_parts.append(f"url('{rel_path}/{font_name}.woff2') format('woff2')")
            if has_woff:
                src_parts.append(f"url('{rel_path}/{font_name}.woff') format('woff')")
            src_line = ",\n               ".join(src_parts)
            code_block = f"""
            @font-face {{
               font-family: '{capital_name}';
               src: {src_line};
               font-weight: {font_weight};
               font-style: {font_style};
               font-display: swap;
             }}
            """

            f.write(code_block)
        f.close()

    woffToCss()
    addToClipBoardFile("fonts.css")
    command = "rm fonts.css"
    os.system(command)
    print("--- %s seconds ---" % (time.time() - start_time))
