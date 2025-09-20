#!/usr/bin/env python3
"""
Script to compile .po files to .mo files using polib
"""
import os
import polib

def compile_po_to_mo(po_file_path):
    """Compile a .po file to a .mo file"""
    try:
        po = polib.pofile(po_file_path)
        mo_file_path = po_file_path.replace('.po', '.mo')
        po.save_as_mofile(mo_file_path)
        print(f"Compiled {po_file_path} -> {mo_file_path}")
        return True
    except Exception as e:
        print(f"Error compiling {po_file_path}: {e}")
        return False

def main():
    """Main function to compile all .po files in the locale directory"""
    locale_dir = os.path.join(os.path.dirname(__file__), 'locale')
    
    if not os.path.exists(locale_dir):
        print(f"Locale directory not found: {locale_dir}")
        return
    
    # Walk through all language directories
    for lang_dir in os.listdir(locale_dir):
        lang_path = os.path.join(locale_dir, lang_dir)
        if os.path.isdir(lang_path):
            lc_messages_path = os.path.join(lang_path, 'LC_MESSAGES')
            if os.path.exists(lc_messages_path):
                po_file = os.path.join(lc_messages_path, 'django.po')
                if os.path.exists(po_file):
                    compile_po_to_mo(po_file)
                else:
                    print(f"No django.po file found in {lc_messages_path}")

if __name__ == '__main__':
    main()