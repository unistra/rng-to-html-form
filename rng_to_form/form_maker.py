def make_form(rng):
    """Takes an rng,  returns a html form.

    Should be reworked.
    """
    results = rng.to_form()
    inside = results['ArchiveTransfer']

    def make_input(value):
        """ depending on what is found in the rng, make the input"""
        what = value[0]
        if what.startswith('not editable'):
            what = what.replace('not editable:', '').replace("'", "\'")
        if what.startswith('attribute:value:'):
            what = what.replace('attribute:value:', '').replace("'", "\'")
        return what

    def walk_dict(target_dict, depth=1):
        """ walks through the dict, makes a form"""
        stuff = ""

        def metadata_in_name(target_string, values):
            """serioulsy"""
            return 0 in [target_string.find(value) for value in values]

        for rng_key, rng_val in sorted(target_dict.items(), key=lambda x: x[0]):
            if isinstance(rng_val, dict):
                cssclass = ""
                if metadata_in_name(rng_key, ['zeroOrMore', 'oneOrMore']):
                    cssclass = "class='multiple'"
                clean_name = rng_key.replace('optional.', '').replace(
                            'oneOrMore.', '').replace('.data', '').replace(
                                'zeroOrMore.', '')
                stuff +="<div class=\"{0}\" >".format(clean_name)
                stuff += "<h{0} {2} rel='togglable' class=\"{3}_rel\">{1}<span class=\"nice-span glyphicon glyphicon-minus\"></span></h{0}>".format(depth, rng_key, cssclass, clean_name)
                stuff += "<div class='holder{}'>".format(depth)
                stuff += walk_dict(rng_val, depth + 1)
            else:
                def find_key(a_dict, key):
                    """find keys"""
                    for his_key, his_val in a_dict.items():
                        if isinstance(his_val, dict):
                            found = find_key(his_val, key)
                            if found:
                                return [his_key] + found
                        elif his_val == key:
                            return [his_key]

                def make_input_name(value):
                    """makes input name"""
                    values = ['optional', 'value',
                              'oneOrMore', 'data', "zeroOrMore"]

                    def strip_meta(this_string):
                        """removes metadata"""
                        wot = this_string.replace('optional', '').replace(
                            'oneOrMore', '').replace('.data', '').replace(
                                'zeroOrMore', '').replace('.', '')
                        return wot
                    ret = [strip_meta(tag) for tag in find_key(inside, value) if tag not in values]
                    return ".".join(ret)

                stuff += "\n<div class=\"{0}\"><div style='font-weight:bold;'>{1}</div>".format(
                                                                                     make_input_name(rng_val),
                    ".".join(find_key(inside, rng_val)))

                def val_starts_with(base_string, strings):
                    """ check if str startswith """
                    for the_string in strings:
                        if base_string.startswith(the_string):
                            return True
                if len(make_input(rng_val)) < 45:
                    if val_starts_with(rng_val[0], ['attribute:value:', 'not editable']):
                        stuff += "<input class='selectable' value=\"{}\" style='width:87%' name=\"{}\" readonly>".format(
                            make_input(rng_val), make_input_name(rng_val))
                    else:
                        stuff += "<input class='selectable' value=\"{}\" style='width:87%' name=\"{}\">".format(
                            "", make_input_name(rng_val))
                else:
                    if val_starts_with(rng_val[0], ['attribute:value:', 'not editable']):
                        stuff += "<textarea class='selectable' rows='8' cols='120' readonly name=\"{1}\">{0}</textarea>".format(
                            make_input(rng_val), make_input_name(rng_val))
                    else:
                        stuff += "<textarea class='selectable' rows='8' cols='120'>{0}</textarea>".format(
                            "")
                stuff += "</div>"
        stuff+="</div>"
        stuff += "</div>"
        return stuff
    return walk_dict(results)
