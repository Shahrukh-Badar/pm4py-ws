from pm4pyws.handlers.parquet.filtering.versions import start_activities, end_activities, attributes_pos_trace, \
    attributes_neg_trace, attributes_pos_events, attributes_neg_events, variants, timestamp_events, \
    timestamp_trace_containing, timestamp_trace_intersecting, case_performance_filter


def apply(dataframe, filter, parameters=None):
    """
    Apply a filter to the current log (factory method)

    Parameters
    ------------
    dataframe
        Pandas dataframe
    filter
        Filter to apply
    parameters
        Parameters of the algorithm

    Returns
    ------------
    dataframe
        Pandas dataframe
    """
    if parameters is None:
        parameters = {}

    if filter[0] == "start_activities":
        return start_activities.apply(dataframe, filter, parameters=parameters)
    elif filter[0] == "end_activities":
        return end_activities.apply(dataframe, filter, parameters=parameters)
    elif filter[0] == "attributes_pos_trace":
        return attributes_pos_trace.apply(dataframe, filter, parameters=parameters)
    elif filter[0] == "attributes_neg_trace":
        return attributes_neg_trace.apply(dataframe, filter, parameters=parameters)
    elif filter[0] == "attributes_pos_events":
        return attributes_pos_events.apply(dataframe, filter, parameters=parameters)
    elif filter[0] == "attributes_neg_events":
        return attributes_neg_events.apply(dataframe, filter, parameters=parameters)
    elif filter[0] == "variants":
        return variants.apply(dataframe, filter, parameters=parameters)
    elif filter[0] == "timestamp_events":
        return timestamp_events.apply(dataframe, filter, parameters=parameters)
    elif filter[0] == "timestamp_trace_containing":
        return timestamp_trace_containing.apply(dataframe, filter, parameters=parameters)
    elif filter[0] == "timestamp_trace_intersecting":
        return timestamp_trace_intersecting.apply(dataframe, filter, parameters=parameters)
    elif filter[0] == "case_performance_filter":
        return case_performance_filter.apply(dataframe, filter, parameters=parameters)

    return dataframe
