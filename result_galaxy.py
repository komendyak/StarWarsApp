
def result_galaxy(galaxy):

    if galaxy == "E0-E2":

        st.title('Elliptical Galaxies : E0-E2')

        st.markdown('Congrats, your galaxy is elliptical (E0-E2) according to the Hubble sequence. Its main characteristics are : no disk, a smooth rounded look. Read below to learn more.')

        st.header('About them')
        st.markdown('Elliptical galaxies have smooth, featureless light distributions and appear as ellipses. \
        The ellipticity increases from left to right on the Hubble diagram, with near-circular (E0) galaxies situated on the very left of the diagram to the most flattened elliptical galaxies (E7) with a cigar shape.\
        They have very little interstellar matter (neither gas nor dust), which results in low rates of star formation, and few young stars.\
        \
        Elliptical galaxies vary greatly in both size and mass with diameters ranging from 3000 lightyears to more than 700,000 lightyears, and masses from 105 to nearly 1013 solar masses. This range is much broader for this galaxy type than for any other. The smallest known elliptical galaxy is about one-tenth the size of the Milky Way.')

        el_schema = Image.open('galaxy_images/elliptical_schema.png')
        st.image(el_schema,use_column_width=True)

        st.header('A few examples of E0-E2 galaxies')
        #import Pil and make an image.open
        E1 = Image.open('galaxy_images/E0-E2.png')
        st.image(E1,use_column_width=True)

    if galaxy == "E3-E5":

        st.title('Elliptical Galaxies : E3-E5')

        st.markdown('Congrats, your galaxy is elliptical (E3-E5) according to the Hubble sequence. Its main characteristics are : no disk, a smooth quite rounded look. Read below to learn more.')

        st.header('About them')
        st.markdown('Elliptical galaxies have smooth, featureless light distributions and appear as ellipses. \
        The ellipticity increases from left to right on the Hubble diagram, with near-circular (E0) galaxies situated on the very left of the diagram to the most flattened elliptical galaxies (E7) with a cigar shape. \
        They have very little interstellar matter (neither gas nor dust), which results in low rates of star formation, and few young stars. \
        \
        Elliptical galaxies vary greatly in both size and mass with diameters ranging from 3000 lightyears to more than 700,000 lightyears, and masses from 105 to nearly 1013 solar masses. This range is much broader for this galaxy type than for any other. The smallest known elliptical galaxy is about one-tenth the size of the Milky Way.')

        el_schema = Image.open('galaxy_images/elliptical_schema.png')
        st.image(el_schema,use_column_width=True)

        st.header('A few examples of E3-E5 galaxies')
        #import Pil and make an image.open
        E3 = Image.open('galaxy_images/E3-E5.png')
        st.image(E3,use_column_width=True)


    if galaxy == "E6-E7":

        st.title('Elliptical Galaxies : E6-E7')

        st.markdown('Congrats, your galaxy is elliptical (E6-E7) according to the Hubble sequence. Its main characteristics are : no disk, a smooth cigar shape. Read below to learn more.')

        st.header('About them')
        st.markdown('Elliptical galaxies have smooth, featureless light distributions and appear as ellipses. \
        The ellipticity increases from left to right on the Hubble diagram, with near-circular (E0) galaxies situated on the very left of the diagram to the most flattened elliptical galaxies (E7) with a cigar shape. \
        They have very little interstellar matter (neither gas nor dust), which results in low rates of star formation, and few young stars. \
         \
        Elliptical galaxies vary greatly in both size and mass with diameters ranging from 3000 lightyears to more than 700,000 lightyears, and masses from 105 to nearly 1013 solar masses. This range is much broader for this galaxy type than for any other. The smallest known elliptical galaxy is about one-tenth the size of the Milky Way.')

        el_schema = Image.open('galaxy_images/elliptical_schema.png')
        st.image(el_schema,use_column_width=True)

        st.header('A few examples of E6-E7 galaxies')
        #import Pil and make an image.open
        E7 = Image.open('galaxy_images/E6-E7.png')
        st.image(E7,use_column_width=True)



    if galaxy == "S0" or value == "SB0":

        st.title('Lenticular Galaxies : S0 and SB0')

        st.markdown('Congrats, your galaxy is lenticular (S0) according to the Hubble sequence. Its main characteristics are : a visible disk and no arms. Read below to learn more.')

        st.header('About them')
        st.markdown('A lenticular galaxy  is a type of galaxy intermediate between an elliptical and a spiral galaxy. It contains a large-scale disc but does not have large-scale spiral arms. They have much higher bulge-to-disk ratios than typical spirals. \
            When simply looking at a galaxy\'s image, lenticular galaxies with relatively face-on disks are difficult to distinguish from ellipticals of type E0–E3 (rounded), making the classification of many such galaxies uncertain. \
            When viewed edge-on, the disk becomes more apparent. Lenticular galaxies are disc galaxies that have used or lost most of their interstellar matter and therefore have very little ongoing star formation. \
         \
            Like spiral galaxies, lenticular galaxies can possess a central bar structure.')

        len_schema = Image.open('galaxy_images/len_schema.png')
        st.image(len_schema,use_column_width=True)

        st.header('A few examples of lenticular galaxies')

        S0 = Image.open('galaxy_images/S0.png')
        st.image(S0,use_column_width=True)



    if galaxy == "Sa/Sb" or value == "Sb/Sc" or value == "ScSd":

        st.title('Spiral Galaxies : Sa/Sb, Sb/Sc, Sc/Sd')

        st.markdown('Congrats, your galaxy is a spiral according to the Hubble sequence. Its main characteristics are : visible arms around a bulge. Read below to learn more.')


        st.header('About them')
        st.markdown('A spiral galaxy consists of a flattened disk (containing stars, gas and dust), with stars forming a spiral structure, and a central concentration of stars known as the bulge. \
            The spiral arms are sites of ongoing star formation and are brighter than the surrounding disc because of the young stars that inhabit them. \
        Together with irregular galaxies, spiral galaxies make up approximately 60% of galaxies in today\'s universe. \
        Roughly 2/3 of all spirals are observed to have a bar-like structure: the Milky Way is a barred spiral (SBc). \
        The oldest spiral galaxy on file is BX442. At eleven billion years old, it is more than two billion years older than any previous discovery.')

        spiral = Image.open('galaxy_images/spiral.png')
        st.image(spiral,use_column_width=True)

        st.header('A few examples of spiral galaxies')
        st.subheader('First type : Sa/Sb spiral galaxies')
        st.markdown('Sa/Sb spirals have tightly wound, smooth arms and a large, bright central bulge')
        sasb = Image.open('galaxy_images/sasb.png')
        st.image(sasb,use_column_width=True,caption="On the left, the Andromeda galaxy that will merge with the Milky Way in about 4 billion years.")

        st.subheader('Second type : Sb/Sc spiral galaxies')
        st.markdown('Sb/Sc have more loose wound spiral arms than Sba, resolving into individual stellar clusters and nebulae, and a smaller, fainter bulge')
        sbsc = Image.open('galaxy_images/sbsc.png')
        st.image(sbsc,use_column_width=True)


        st.subheader('Third type : Sc/Sd spiral galaxies')
        st.markdown('Sc/Sd spirals have very loosely wound, fragmentary arms, most of the luminosity is in the arms and not the bulge')
        scsd = Image.open('galaxy_images/scsd.png')
        st.image(scsd,use_column_width=True, caption="Left and middle: BX442, the oldest known spiral galaxy today.")


    if galaxy == "SBa/SBb" or value == "SBb/SBc" or value == "SBcSBd":

        st.title('Barred Spiral Galaxies : SBa/SBb, SBb/SBc, SBc/SBd')

        st.markdown('Congrats, your galaxy is a barred spiral according to the Hubble sequence. Its main characteristics are : visible arms around a bulge and a bar feature. Read below to learn more.')

        st.header('About them')
        st.markdown('A spiral galaxy consists of a flattened disk (containing stars, gas and dust), with stars forming a spiral structure, and a central concentration of stars known as the bulge. \
        The spiral arms are sites of ongoing star formation and are brighter than the surrounding disc because of the young stars that inhabit them. Together with irregular galaxies, spiral galaxies make up approximately 60\% of galaxies in today\'s universe. \
        Roughly 2/3 of all spirals are observed to have a bar-like structure, with the bar extending from the central bulge, and the arms begin at the ends of the bar. The proportion of barred spirals relative to barless spirals has increased over the history of the universe: only 10% contained bars 8 billion years ago. \
        The Milky Way is a barred spiral (SBc), although the bar itself is difficult to observe from Earth\'s current position within the galactic disc.')

        bspiral = Image.open('galaxy_images/bspiral.png')
        st.image(bspiral,use_column_width=True)

        st.header('A few examples of barred spiral galaxies')
        st.subheader('First type : SBa/SBb barred spiral galaxies')
        st.markdown('Sba/SBb spirals have tightly wound, smooth arms and a large, bright central bulge')
        sbasbb = Image.open('galaxy_images/sbasbb.png')
        st.image(sbasbb,use_column_width=True)

        st.subheader('First type : SBb/SBc barred spiral galaxies')
        st.markdown('SBb/SBc have more loose wound spiral arms than Sba, resolving into individual stellar clusters and nebulae, and a smaller, fainter bulge')
        sbbsbc = Image.open('galaxy_images/sbbsbc.png')
        st.image(sbbsbc,use_column_width=True, caption = "On the left : the Milky Way, aka home.")

        st.subheader('First type : SBc/SBd barred spiral galaxies')
        st.markdown('SBc/SBd spirals have very loosely wound, fragmentary arms, most of the luminosity is in the arms and not the bulge')
        sbcsbd = Image.open('galaxy_images/sbcsbd.png')
        st.image(sbcsbd,use_column_width=True, caption = "On the left, NGC 1300, a grand design galaxy")

    if galaxy == "irregular" or value == "merger":

        st.title('Irregular Galaxies')

    st.markdown('Congrats, your galaxy is irregular according to the Hubble sequence. They don\'t have main characteristics, appart from looking quite chaotic and having no identified features. Read below to learn more.')

        st.header('About them')
        st.markdown('Galaxies that do not fit into the Hubble sequence because they have no regular structure (either disk-like or ellipsoidal) are irregular galaxies. They are often chaotic in appearance: they have an asymmetric profile and lack a central bulge or obvious spiral structure. Instead, they contain many individual clusters of young stars. \
            They are thought to make up about a quarter of all galaxies. Some irregular galaxies were once spiral or elliptical galaxies but were deformed by an uneven external gravitational force. Irregular galaxies may contain abundant amounts of gas and dust. \
            Irregular galaxies are commonly small, about one tenth the mass of the Milky Way galaxy (our galaxy!). Due to their small sizes, they are prone to environmental effects like crashing with large galaxies and intergalactic clouds. \
            ')

        irr = Image.open('galaxy_images/irr.png')
        st.image(irr,use_column_width=True)

        st.header('Have a look at these impressive examples of other irregular galaxies:')

        irregulars = Image.open('galaxy_images/irregulars.png')
        st.image(irregulars,use_column_width=True)

    if galaxy == "dust lane" or value == "lens or an arc":
        st.title('I am sorry but ...')
        st.header("... we cannot identify a galaxy there.")
        st.markdown("Or maybe the telescope that took the picture was not perfectly clean, or captured other elements.")


    if galaxy == "ring":
        st.title("Ring galaxies")

        st.markdown('It looks like your galaxy is a ring galaxy. It has a visible ring with no bulge, but it does not belong to the Hubble sequence. Read below to learn more.')

        st.header('About them')
        st.markdown("A ring galaxy is a galaxy with a circle-like appearance. Hoag's Object, discovered by Art Hoag in 1950, is an example of a ring galaxy. This galaxy does not fit in the Hubble classification.")

        ring = Image.open('galaxy_images/ring.png')
        st.image(ring,use_column_width=True, caption = "Hoag's Object")
